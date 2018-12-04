"""
Controll device settings on the unit.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import asyncio
from socket import gaierror
import aiohttp
import async_timeout
from googledevices.utils.const import API, HEADERS
from googledevices.utils.exceptions import ConnectionException


class DeviceSettings(object):
    """A class for device dettings."""

    def __init__(self, loop, session, ipaddress):
        """Initialize the class."""
        self._loop = loop
        self._ipaddress = ipaddress
        self._session = session

    async def reboot(self):
        """Reboot the device."""
        endpoint = '/setup/reboot'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        data = {'params': 'now'}
        returnvalue = False
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                result = await self._session.post(url, json=data,
                                                  headers=HEADERS)
                if result.status == 200:
                    returnvalue = True
        except (asyncio.TimeoutError, aiohttp.ClientError, gaierror) as error:
            raise ConnectionException(self._ipaddress, error)
        return returnvalue

    async def set_eureka_info(self, data):
        """Set eureka info."""
        endpoint = '/setup/set_eureka_info'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        returnvalue = False
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                result = await self._session.post(url, json=data,
                                                  headers=HEADERS)
                if result.status == 200:
                    returnvalue = True
        except (asyncio.TimeoutError, aiohttp.ClientError, gaierror) as error:
            raise ConnectionException(self._ipaddress, error)
        return returnvalue

    async def control_notifications(self, active):
        """Set control_notifications option."""
        endpoint = '/setup/set_eureka_info'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        value = 1 if active else 2
        data = {'settings': {'control_notifications': value}}
        returnvalue = False
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                result = await self._session.post(url, json=data,
                                                  headers=HEADERS)
                if result.status == 200:
                    returnvalue = True
        except (asyncio.TimeoutError, aiohttp.ClientError, gaierror) as error:
            raise ConnectionException(self._ipaddress, error)
        return returnvalue
