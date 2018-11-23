"""Example usage of googledevices."""
import asyncio
import aiohttp
from googledevices.bluetooth import Bluetooth
from googledevices.scan import NetworkScan
from googledevices.device_info import DeviceInfo

IPRANGE = '192.168.2.0/24'


async def bluetooth_scan():
    """
    Get devices from all GH units on the network.

    This will scan the IPRANGE defined above for GH units.
    Then do a multirun scan on each unit.
    Compiling all devices from all units so you can see which unit has
    the stronges signal to the device.
    """
    devices = {}
    async with aiohttp.ClientSession() as session:
        googledevices = NetworkScan(LOOP, session)
        result = await googledevices.scan_for_units(IPRANGE)
    for host in result:
        if host['assistant_supported']:
            async with aiohttp.ClientSession() as session:
                googledevices = DeviceInfo(LOOP, session, host['host'])
                await googledevices.get_device_info()
                ghname = googledevices.device_info.get('name')
            async with aiohttp.ClientSession() as session:
                googledevices = Bluetooth(LOOP, session, host['host'])
                await googledevices.scan_for_devices_multi_run()
                await googledevices.get_scan_result()
                for device in googledevices.devices:
                    mac = device['mac_address']
                    if not devices.get(mac, False):
                        # New device
                        devices[mac] = {}
                        devices[mac]['rssi'] = device['rssi']
                        devices[mac]['ghunit'] = ghname
                    elif devices[mac]['rssi'] < device['rssi']:
                        # Better RSSI value on this device
                        devices[mac]['rssi'] = device['rssi']
                        devices[mac]['ghunit'] = ghname
    print(devices)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(bluetooth_scan())
