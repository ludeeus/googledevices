"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.bluetooth import Bluetooth

IPADDRESS = '192.168.2.234'


async def test_bluetooth():
    """Get nearby bluetooth devices."""
    async with aiohttp.ClientSession() as session:
        bluetooth = Bluetooth(LOOP, session, IPADDRESS)
        await bluetooth.scan_for_devices()  # Start device scan.
        await bluetooth.get_scan_result()  # Returns the result after that scan.

        print("Device info:", bluetooth.devices)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test_bluetooth())
