"""Reboot a Google device."""
from aiohttp import ClientSession


def reboot(loop, ip_address):
    """Reboot a Google device."""
    from googledevices.api.device_settings import DeviceSettings

    async def reboot_device():
        """Reboot a Google Home unit."""
        async with ClientSession() as session:
            googledevices = DeviceSettings(loop, session, ip_address)
            await googledevices.reboot()
    loop.run_until_complete(reboot_device())
