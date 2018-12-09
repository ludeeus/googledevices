"""Get information from Google WiFi."""
from json import dumps
from aiohttp import ClientSession


def get_wifi_info(loop, ip_address):
    """Get information from Google WiFi."""
    from googledevices.api.googlewifi import Info

    async def wifi():
        """Get information from Google WiFi."""
        async with ClientSession() as session:
            googledevices = Info(loop, session, ip_address)
            await googledevices.get_wifi_info()
            print(dumps(googledevices.wifi_info, indent=4, sort_keys=True))
    loop.run_until_complete(wifi())


def get_wifi_devices(loop, ip_address, show):
    """Get devices from Google WiFi."""
    from googledevices.api.googlewifi import Devices

    async def devices():
        """Get information from Google WiFi."""
        async with ClientSession() as session:
            googledevices = Devices(loop, session, ip_address)
            print("This command will take some time (10+ seconds) to finish.")
            await googledevices.get_devices()
            if show == 'mac':
                devices = []
                for device in googledevices.devices:
                    devices.append(device['mac'])
            elif show == 'ip':
                devices = []
                for device in googledevices.devices:
                    devices.append(device['ip'])
            else:
                devices = googledevices.devices
            print(dumps(devices, indent=4, sort_keys=True))
    loop.run_until_complete(devices())
