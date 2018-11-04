"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.bluetooth import BluetoothScan

IPADDRESS = '192.168.2.234'


async def test():
    """Example usage of ghlocalapi."""
    async with aiohttp.ClientSession() as session:
        data = BluetoothScan(LOOP, session, IPADDRESS)
        await data.scan_for_devices()  # Start device scan.
        await data.get_scan_result()  # Returns the result after that scan.

        print("Device info:", data.devices)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test())
