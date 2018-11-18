"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.alarms import Alarms

IPADDRESS = '192.168.2.234'


async def get_alarms():
    """Get alarms and timers from GH."""
    async with aiohttp.ClientSession() as session:
        alarms = Alarms(LOOP, session, IPADDRESS)
        await alarms.get_alarms()

        print("Alarms:", alarms.alarms)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(get_alarms())
