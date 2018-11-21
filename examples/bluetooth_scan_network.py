"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.bluetooth import Bluetooth
from ghlocalapi.scan import NetworkScan
from ghlocalapi.device_info import DeviceInfo

IPRANGE = '192.168.2.0/24'


async def bluetooth_scan():
    """
    This will scan the IPRANGE defined above for GH units.
    Then do a multirun scan on each unit.
    Compiling all devices from all units so you can see which unit has
    the stronges signal to the device.
    """
    devices = {}
    async with aiohttp.ClientSession() as session:
        ghlocalapi = NetworkScan(LOOP, session)
        result = await ghlocalapi.scan_for_units(IPRANGE)
    for host in result:
        if host['assistant_supported']:
            async with aiohttp.ClientSession() as session:
                ghlocalapi = DeviceInfo(LOOP, session, host['host'])
                await ghlocalapi.get_device_info()
                ghname = ghlocalapi.device_info.get('name')
            async with aiohttp.ClientSession() as session:
                ghlocalapi = Bluetooth(LOOP, session, host['host'])
                await ghlocalapi.scan_for_devices_multi_run()
                await ghlocalapi.get_scan_result()
                for device in ghlocalapi.devices:
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
