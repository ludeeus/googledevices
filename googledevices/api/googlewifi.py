"""
Get device information from Google WiFi.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import asyncio
from socket import gaierror
import aiohttp
import async_timeout
from googledevices.utils.const import GOOGLE_WIFI_API, WIFI_HOSTS
from googledevices.utils.exceptions import ConnectionException


class Info(object):
    """A class for device info."""

    def __init__(self, loop, session, ipaddress=None):
        """Initialize the class."""
        self._loop = loop
        self._ipaddress = ipaddress
        self._session = session
        self._wifi_host = None
        self._wifi_info = {}
        self._devices = []

    async def get_host(self):
        """Get the hostname/IP of the WiFi unit."""
        hosts = WIFI_HOSTS
        if self._ipaddress is not None:
            self._wifi_host = self._ipaddress
        else:
            for host in hosts:
                url = GOOGLE_WIFI_API.format(ip=host, endpoint='status')
                try:
                    async with async_timeout.timeout(5, loop=self._loop):
                        await self._session.get(url)
                        self._wifi_host = host
                except (asyncio.TimeoutError, aiohttp.ClientError,
                        gaierror):
                    self._wifi_host = None
        return self._wifi_host

    async def get_wifi_info(self):
        """Get the bluetooth status of the device."""
        if self._wifi_host is None:
            await self.get_host()
        url = GOOGLE_WIFI_API.format(ip=self._wifi_host, endpoint='status')
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)
                self._wifi_info = await response.json()
        except (asyncio.TimeoutError, aiohttp.ClientError, gaierror) as error:
            raise ConnectionException(self._ipaddress, error)
        return self.wifi_info

    @property
    def wifi_host(self):
        """Return the hostname or IP of the device."""
        return self._wifi_host

    @property
    def wifi_info(self):
        """Return the device info if any."""
        return self._wifi_info


class Devices(object):
    """A class for devices."""

    def __init__(self, loop, session, ipaddress=None):
        """Initialize the class."""
        self.info = Info(loop, session)
        self._ipaddress = ipaddress
        self._wifi_host = None
        self._devices = []

    async def get_devices(self):
        """Return devices form the network."""
        import requests
        self._devices = []
        if self.info.wifi_host is None:
            await self.info.get_host()
        url = GOOGLE_WIFI_API.format(ip=self.info.wifi_host,
                                     endpoint='diagnostic-report')
        try:
            response = requests.request("GET", url)
            all_devices = response.text
            all_devices = all_devices.split('/proc/net/arp')[1]
            all_devices = all_devices.split('/proc/slabinfo')[0]
            all_devices = all_devices.splitlines()
            for device in all_devices[1:-2]:
                ip_address = device.split()[0]
                mac = device.split()[3]
                info = {'ip': ip_address, 'mac': mac}
                self._devices.append(info)
        except (asyncio.TimeoutError, aiohttp.ClientError, gaierror) as error:
            raise ConnectionException(self._ipaddress, error)
        return self._devices

    @property
    def devices(self):
        """Return devices form the network."""
        return self._devices
