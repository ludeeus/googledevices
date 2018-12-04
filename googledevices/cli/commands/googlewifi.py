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
