"""Example usage of googledevices."""
import asyncio
import time
import aiohttp
from googledevices.api.bluetooth import Bluetooth

IPADDRESS = '192.168.2.234'


async def bluetooth_scan():
    """Get nearby bluetooth devices."""
    async with aiohttp.ClientSession() as session:
        googledevices = Bluetooth(LOOP, session, IPADDRESS)
        await googledevices.scan_for_devices()  # Start device scan
        time.sleep(5)
        await googledevices.get_scan_result()  # Returns the result

        print("Device info:", googledevices.devices)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(bluetooth_scan())
