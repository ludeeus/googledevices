"""Get bluetooth devices from a unit."""
from asyncio import sleep
from json import dumps
from aiohttp import ClientSession


def get_bluetooth_devices(loop, ip_address):
    """Get bluetooth devices from a unit."""
    from googledevices.api.bluetooth import Bluetooth

    async def bluetooth_scan():
        """Get nearby bluetooth devices."""
        async with ClientSession() as session:
            googledevices = Bluetooth(loop, session, ip_address)
            await googledevices.scan_for_devices()
            await sleep(5)
            await googledevices.get_scan_result()
            print(dumps(googledevices.devices, indent=4, sort_keys=True))
    loop.run_until_complete(bluetooth_scan())
