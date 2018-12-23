"""Retrieve alarms from Google Home."""
from googledevices.utils.const import HEADERS, CASTPORT
import googledevices.utils.log as log
from googledevices.helpers import gdh_request


class Alarm(object):
    """A class for getting the alarms from a Google Home."""

    def __init__(self, host, loop, session):
        """Initialize the class."""
        self.loop = loop
        self.host = host
        self.session = session
        self._alarms = []
        self._alarmvolume = None

    async def get_alarms(self):
        """Get the alarms from the device."""
        endpoint = 'setup/assistant/alarms'
        response = await gdh_request(host=self.host, port=CASTPORT,
                                     loop=self.loop, session=self.session,
                                     endpoint=endpoint)
        self._alarms = response
        log.debug(self._alarms)
        return self._alarms

    async def get_alarm_volume(self):
        """Get the alarm volume for the device."""
        endpoint = 'setup/assistant/alarms/volume'
        response = await gdh_request(host=self.host, port=CASTPORT,
                                     loop=self.loop, session=self.session,
                                     endpoint=endpoint, method='post')
        self._alarmvolume = response
        log.debug(self._alarmvolume)
        return self._alarmvolume

    async def set_alarm_volume(self, volume):
        """Set the alarm volume for the device."""
        data = {'volume': volume}
        endpoint = 'setup/assistant/alarms/volume'
        returnvalue = False
        result = await gdh_request(host=self.host, port=CASTPORT,
                                   endpoint=endpoint, method='post',
                                   loop=self.loop, session=self.session,
                                   json_data=data, headers=HEADERS,
                                   json=False)
        try:
            if result.status == 200:
                returnvalue = True
        except AttributeError:
            msg = "Error connecting to - {}".format(self.host)
            log.error(msg)
        return returnvalue

    @property
    def alarms(self):
        """Return the alarms."""
        return self._alarms

    @property
    def alarm_volume(self):
        """Return the alarm volume."""
        return self._alarmvolume
