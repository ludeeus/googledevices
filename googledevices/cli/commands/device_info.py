"""Get information about a Google device on your network."""
from json import dumps
from aiohttp import ClientSession


def device_info(loop, ip_address):
    """Get information about a Google device on your network."""
    from googledevices.api.device_info import DeviceInfo

    async def get_device_info():
        """Get device info."""
        async with ClientSession() as session:
            googledevices = DeviceInfo(loop, session, ip_address)
            await googledevices.get_device_info()
            print(dumps(googledevices.device_info,
                        indent=4, sort_keys=True))
    loop.run_until_complete(get_device_info())
