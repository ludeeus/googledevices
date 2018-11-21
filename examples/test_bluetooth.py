"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.bluetooth import Bluetooth

IPADDRESS = '192.168.2.234'


async def test_bluetooth():
    """Get nearby bluetooth devices."""
    async with aiohttp.ClientSession() as session:
        ghlocalapi = Bluetooth(LOOP, session, IPADDRESS)
        await ghlocalapi.scan_for_devices()  # Start device scan
        await ghlocalapi.get_scan_result()  # Returns the result

        print("Device info:", ghlocalapi.devices)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test_bluetooth())
