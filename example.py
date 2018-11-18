"""Example usage of ghlocalapi."""
import asyncio
import aiohttp
from ghlocalapi.bluetooth import Bluetooth
from ghlocalapi.alarms import Alarms

IPADDRESS = '192.168.2.234'


async def test_bluetooth():
    """Example usage of ghlocalapi bluetooth."""
    async with aiohttp.ClientSession() as session:
        data = Bluetooth(LOOP, session, IPADDRESS)
        await data.scan_for_devices()  # Start device scan.
        await data.get_scan_result()  # Returns the result after that scan.

        print("Device info:", data.devices)


async def test_alarms():
    """Example usage of ghlocalapi alarms."""
    async with aiohttp.ClientSession() as session:
        data = Alarms(LOOP, session, IPADDRESS)
        await data.get_alarms() # Returns active alarms and timers.

        print("Alarms:", data.alarms)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test_bluetooth())
LOOP.run_until_complete(test_alarms())
