"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.device_info import DeviceInfo

IPADDRESS = '192.168.2.234'


async def device_info():
    """Get device info from GH."""
    async with aiohttp.ClientSession() as session:
        ghlocalapi = DeviceInfo(LOOP, session, IPADDRESS)
        await ghlocalapi.get_device_info()

        print("Device info:", ghlocalapi.device_info)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(device_info())
