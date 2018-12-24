"""
This serves as a brige to all classes.

This can connect to all classes in the package.
"""


class Cast(object):
    """Cast class for ChromeCast and Google Home units."""

    def __init__(self, host=None, loop=None, session=None):
        """Initialize the class."""
        self.host = host
        self.loop = loop
        self.session = session

    async def bluetooth(self):
        """Return cast Bluetooth connector."""
        from googledevices.api.cast.bluetooth import Bluetooth
        return Bluetooth(self.host, self.loop, self.session)

    async def info(self):
        """Return cast DeviceInfo connector."""
        from googledevices.api.cast.info import Info
        return Info(self.host, self.loop, self.session)

    async def settings(self):
        """Return cast DeviceSettings connector."""
        from googledevices.api.cast.settings import Settings
        return Settings(self.host, self.loop, self.session)

    async def assistant(self):
        """Return cast DeviceSettings connector."""
        from googledevices.api.cast.assistant import Assistant
        return Assistant(self.host, self.loop, self.session)

    async def wifi(self):
        """Return cast DeviceSettings connector."""
        from googledevices.api.cast.wifi import Wifi as CastWifi
        return CastWifi(self.host, self.loop, self.session)


class Wifi(object):
    """Wifi class for Google WiFi."""

    def __init__(self, host=None, loop=None, session=None):
        """Initialize the class."""
        self.host = host
        self.loop = loop
        self.session = session

    async def clients(self):
        """Return cast DeviceSettings connector."""
        from googledevices.api.wifi.clients import Clients
        return Clients(self.host, self.loop, self.session)

    async def info(self):
        """Return cast DeviceSettings connector."""
        from googledevices.api.wifi.info import Info
        return Info(self.host, self.loop, self.session)
