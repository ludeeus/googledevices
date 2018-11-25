"""Example usage of googledevices."""
import asyncio
import aiohttp
from googledevices.api.device_settings import DeviceSettings

IPADDRESS = '192.168.2.234'


async def reboot():
    """Reboot a Google Home unit."""
    async with aiohttp.ClientSession() as session:
        googledevices = DeviceSettings(LOOP, session, IPADDRESS)
        result = await googledevices.reboot()

        print("Reboot info:", result)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(reboot())
