"""Controll device settings on the unit."""
from googledevices.utils.const import CASTPORT, CAST_HEADERS
from googledevices.helpers import gdh_request
import googledevices.utils.log as log


class Settings(object):
    """A class for device settings."""

    def __init__(self, host, loop, session, test):
        """Initialize the class."""
        self.host = host
        self.loop = loop
        self.session = session
        self.port = None if test else CASTPORT

    async def reboot(self, mode='now'):
        """Reboot the device."""
        endpoint = 'setup/reboot'
        supported_modes = ['now', 'fdr']
        returnvalue = False
        if mode not in supported_modes:
            log_msg = "Mode {} is not supported.".format(mode)
            log.error(log_msg)
            return returnvalue
        data = {'params': mode}
        result = await gdh_request(host=self.host, port=self.port,
                                   endpoint=endpoint, method='post',
                                   loop=self.loop, session=self.session,
                                   json_data=data, headers=CAST_HEADERS,
                                   json=False)
        try:
            if result.status == 200:
                returnvalue = True
        except AttributeError:
            msg = "Error connecting to - {}".format(self.host)
            log.error(msg)
        return returnvalue

    async def set_eureka_info(self, data):
        """Set eureka info."""
        endpoint = 'setup/set_eureka_info'
        returnvalue = False
        result = await gdh_request(host=self.host, port=self.port,
                                   endpoint=endpoint, method='post',
                                   loop=self.loop, session=self.session,
                                   json_data=data, headers=CAST_HEADERS,
                                   json=False)
        try:
            if result.status == 200:
                returnvalue = True
        except AttributeError:
            msg = "Error connecting to - {}".format(self.host)
            log.error(msg)
        return returnvalue

    async def control_notifications(self, active):
        """Set control_notifications option."""
        endpoint = 'setup/set_eureka_info'
        value = 1 if active else 2
        data = {'settings': {'control_notifications': value}}
        returnvalue = False
        result = await gdh_request(host=self.host, port=self.port,
                                   endpoint=endpoint, method='post',
                                   loop=self.loop, session=self.session,
                                   json_data=data, headers=CAST_HEADERS,
                                   json=False)
        try:
            if result.status == 200:
                returnvalue = True
        except AttributeError:
            msg = "Error connecting to - {}".format(self.host)
            log.error(msg)
        return returnvalue
