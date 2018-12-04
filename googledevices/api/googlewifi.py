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
