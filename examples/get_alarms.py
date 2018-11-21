"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.alarms import Alarms

IPADDRESS = '192.168.2.234'


async def get_alarms():
    """Get alarms and timers from GH."""
    async with aiohttp.ClientSession() as session:
        ghlocalapi = Alarms(LOOP, session, IPADDRESS)
        await ghlocalapi.get_alarms()

        print("Alarms:", ghlocalapi.alarms)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(get_alarms())
