"""Example usage of googledevices."""
from aiohttp import ClientSession
from googledevices.api.alarms import Alarms


def alarm_volume(loop, ip_address, mode, volume=None):
    """Handle alarm volume."""
    async def set_alarm_volume():
        """Get alarms and timers from GH."""
        async with ClientSession() as session:
            googledevices = Alarms(loop, session, ip_address)
            await googledevices.set_alarm_volume(None)

    async def get_alarm_volume():
        """Get alarms and timers from GH."""
        async with ClientSession() as session:
            googledevices = Alarms(loop, session, ip_address)
            await googledevices.get_alarm_volume()
            print("Volume:", googledevices.alarm_volume)

    if mode == 'set':
        if volume is None:
            print("You need to supply a volume like '--volume 0.8'")
            return
        loop.run_until_complete(set_alarm_volume())
    else:
        loop.run_until_complete(get_alarm_volume())
