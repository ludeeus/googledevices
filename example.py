"""Example usage of GHLocalApi."""
import asyncio
import aiohttp
from ghlocalapi.bluetooth import BluetoothScan

IPADDRESS = '192.168.2.234'


async def test():
    """Example usage of GHLocalApi."""
    async with aiohttp.ClientSession() as session:
        data = BluetoothScan(LOOP, session, IPADDRESS)
        await data.scan_for_devices()
        await data.get_scan_result()

        print("Device info:", data.devices)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test())
