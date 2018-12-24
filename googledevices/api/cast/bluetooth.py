"""Bluetooth handling on Google Home units."""
from googledevices.helpers import gdh_request
from googledevices.utils.const import HEADERS, CASTPORT
import googledevices.utils.log as log


class Bluetooth(object):
    """A class for Bluetooth scan ."""

    def __init__(self, host, loop, session):
        """Initialize the class."""
        self.loop = loop
        self.host = host
        self.session = session
        self._devices = []
        self._paired_devices = []
        self._status = {}

    async def get_bluetooth_status(self):
        """Get the bluetooth status of the device."""
        endpoint = 'setup/bluetooth/status'
        response = await gdh_request(host=self.host, port=CASTPORT,
                                     loop=self.loop, session=self.session,
                                     endpoint=endpoint, headers=HEADERS)
        self._status = response
        log.debug(self._status)
        return self._status

    async def get_paired_devices(self):
        """Get paired devices."""
        endpoint = 'setup/bluetooth/get_bonded'
        response = await gdh_request(host=self.host, port=CASTPORT,
                                     loop=self.loop, session=self.session,
                                     endpoint=endpoint, headers=HEADERS)
        self._status = response
        log.debug(self._status)
        return self._status

    async def forget_paired_device(self, mac_address):
        """Forget a paired device."""
        endpoint = 'setup/bluetooth/bond'
        data = {"bond": False, "mac_address": mac_address}
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

    async def set_discovery_enabled(self):
        """Enable bluetooth discoverablility."""
        endpoint = 'setup/bluetooth/discovery'
        data = {"enable_discovery": True}
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

    async def pair_with_mac(self, mac_address):
        """Pair with bluetooth device."""
        endpoint = 'setup/bluetooth/scan'
        data = {"connect": True, "mac_address": mac_address, "profile": 2}
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

    async def scan_for_devices(self):
        """Scan for bluetooth devices."""
        endpoint = 'setup/bluetooth/scan'
        data = {"enable": True, "clear_results": True, "timeout": 5}
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

    async def get_scan_result(self):
        """Scan for bluetooth devices."""
        endpoint = 'setup/bluetooth/scan_results'
        response = await gdh_request(host=self.host, port=CASTPORT,
                                     loop=self.loop, session=self.session,
                                     endpoint=endpoint, headers=HEADERS)
        self._devices = response
        log.debug(self._devices)
        return self._devices

    @property
    def status(self):
        """Return the the bluetooth status of the device."""
        return self._status

    @property
    def devices(self):
        """Return the devices if any."""
        return self._devices

    @property
    def paired_devices(self):
        """Return paired devices if any."""
        return self._paired_devices
