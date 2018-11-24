"""Example usage of googledevices."""
import asyncio
import aiohttp
from googledevices.utils.scan import NetworkScan

IPRANGE = '192.168.2.0/24'


async def device_info():
    """Get device info from GH."""
    async with aiohttp.ClientSession() as session:
        googledevices = NetworkScan(LOOP, session)
        result = await googledevices.scan_for_units(IPRANGE)
        print(result)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(device_info())
