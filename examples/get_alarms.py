"""Example usage of googledevices."""
import asyncio
import aiohttp
from googledevices.api.alarms import Alarms

IPADDRESS = '192.168.2.234'


async def get_alarms():
    """Get alarms and timers from GH."""
    async with aiohttp.ClientSession() as session:
        googledevices = Alarms(LOOP, session, IPADDRESS)
        await googledevices.get_alarms()

        print("Alarms:", googledevices.alarms)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(get_alarms())
