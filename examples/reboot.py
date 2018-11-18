"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.device_settings import DeviceSettings

IPADDRESS = '192.168.2.234'


async def reboot():
    """Reboot a Google Home unit."""
    async with aiohttp.ClientSession() as session:
        device_settings = DeviceSettings(LOOP, session, IPADDRESS)
        result = await device_settings.reboot()

        print("Reboot info:", result)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(reboot())
