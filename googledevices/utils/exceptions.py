"""Exceptions for googledevices."""
import googledevices.utils.log as log


class GoogleDevicesExcetion(Exception):
    """Define a base error."""


class ConnectionException(GoogleDevicesExcetion):
    """Define an error related to conncetion issues."""

    async def __init__(self, host, message):
        """Initialize this class."""
        GoogleDevicesExcetion.__init__()
        self.host = host
        self.message = message
        self.log()

    async def log(self):
        """Print log."""
        logmessage = 'Error connecting to {} - {}'.format(self.host,
                                                          self.message)
        log.error(logmessage)
