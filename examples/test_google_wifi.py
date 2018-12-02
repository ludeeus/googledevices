"""Example usage of googledevices."""
import asyncio
import aiohttp
from googledevices.api.googlewifi import Info


async def wifi():
    """Get information from Google WiFi."""
    async with aiohttp.ClientSession() as session:
        googledevices = Info(LOOP, session)
        await googledevices.get_wifi_info()
        print("Info:", googledevices.wifi_info)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(wifi())
