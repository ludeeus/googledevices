"""Example usage of googledevices."""
import asyncio
import aiohttp
from googledevices.api.alarms import Alarms

IPADDRESS = '192.168.2.234'


async def set_alarm_volume():
    """Get alarms and timers from GH."""
    async with aiohttp.ClientSession() as session:
        googledevices = Alarms(LOOP, session, IPADDRESS)
        await googledevices.set_alarm_volume(0.8)


async def get_alarm_volume():
    """Get alarms and timers from GH."""
    async with aiohttp.ClientSession() as session:
        googledevices = Alarms(LOOP, session, IPADDRESS)
        await googledevices.get_alarm_volume()

        print("Volume:", googledevices.alarm_volume)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(get_alarm_volume())
LOOP.run_until_complete(set_alarm_volume())
