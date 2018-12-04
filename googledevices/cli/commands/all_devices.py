"""Get information about all devices on your network."""
from asyncio import sleep
from json import dumps
from aiohttp import ClientSession


def get_all_devices(loop, subnet):
    """Get information about all devices on your network."""
    from googledevices.api.bluetooth import Bluetooth
    from googledevices.utils.scan import NetworkScan
    from googledevices.api.device_info import DeviceInfo
    devices = {}

    async def get_device_info(host):
        """Grab device information."""
        async with ClientSession() as session:
            googledevices = DeviceInfo(loop, session, host['host'])
            await googledevices.get_device_info()
            ghname = googledevices.device_info.get('name')
        async with ClientSession() as session:
            googledevices = Bluetooth(loop, session, host.get('host'))
            await googledevices.scan_for_devices_multi_run()
            await sleep(5)
            await googledevices.get_scan_result()
            for device in googledevices.devices:
                mac = device['mac_address']
                if not devices.get(mac, False):
                    # New device
                    devices[mac] = {}
                    devices[mac]['rssi'] = device.get('rssi')
                    devices[mac]['ghunit'] = ghname
                elif devices[mac].get('rssi') < device.get('rssi'):
                    # Better RSSI value on this device
                    devices[mac]['rssi'] = device.get('rssi')
                    devices[mac]['ghunit'] = ghname

    async def bluetooth_scan():
        """Get devices from all GH units on the network."""
        if not subnet:
            import netifaces
            gateway = netifaces.gateways().get('default', {})
            ipscope = gateway.get(netifaces.AF_INET, ())[0][:-1] + '0/24'
        else:
            ipscope = subnet
        async with ClientSession() as session:
            googledevices = NetworkScan(loop, session)
            result = await googledevices.scan_for_units(ipscope)
        for host in result:
            if host['bluetooth']:
                get_device_info(host)
        print(dumps(devices, indent=4, sort_keys=True))
    loop.run_until_complete(bluetooth_scan())
