"""Example usage of googledevices."""
import asyncio
import aiohttp
from googledevices.device_info import DeviceInfo

IPADDRESS = '192.168.2.234'


async def device_info():
    """Get device info from GH."""
    async with aiohttp.ClientSession() as session:
        googledevices = DeviceInfo(LOOP, session, IPADDRESS)
        await googledevices.get_device_info()

        print("Device info:", googledevices.device_info)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(device_info())
