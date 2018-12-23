"""Get device information for the unit."""
from googledevices.utils.const import DEFAULT_DEVICE_NAME, CASTPORT
import googledevices.utils.log as log
from googledevices.helpers import gdh_request


class Info(object):
    """A class for device info."""

    def __init__(self, host, loop, session):
        """Initialize the class."""
        self.loop = loop
        self.host = host
        self.session = session
        self._name = 'GoogleDevice'
        self._device_info = {}

    async def get_device_info(self):
        """Get device information for the unit.."""
        endpoint = 'setup/eureka_info'
        params = ("params=version,audio,name,build_info,detail,device_info,"
                  "net,wifi,setup,settings,opt_in,opencast,multizone,proxy,"
                  "night_mode_params,user_eq,room_equalizer&options=detail")
        response = await gdh_request(host=self.host, port=CASTPORT,
                                     loop=self.loop, session=self.session,
                                     endpoint=endpoint, params=params)
        self._device_info = response
        log.debug(self._device_info)
        return self._device_info

    @property
    def device_info(self):
        """Return the device info if any."""
        return self._device_info

    @property
    def name(self):
        """Return the device name."""
        return self._device_info.get('name', DEFAULT_DEVICE_NAME)
