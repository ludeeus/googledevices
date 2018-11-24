"""
Retrieve alarms from Google Home.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import asyncio
import logging
import socket

import aiohttp
import async_timeout

from googledevices.utils.const import API, HEADERS

_LOGGER = logging.getLogger(__name__)


class Alarms(object):
    """A class for getting the alarms from a Google Home."""

    def __init__(self, loop, session, ipaddress):
        """Initialize the class."""
        self._loop = loop
        self._ipaddress = ipaddress
        self._session = session
        self._alarms = []
        self._alarmvolume = None

    async def get_alarms(self):
        """Get the alarms from the device."""
        endpoint = '/setup/assistant/alarms'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)
                self._alarms = await response.json()
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to googledevices, %s', error)

    async def get_alarm_volume(self):
        """Get the alarm volume for the device."""
        endpoint = '/setup/assistant/alarms/volume'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.post(url, headers=HEADERS)
                self._alarmvolume = await response.json()
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to googledevices, %s', error)

    async def set_alarm_volume(self, volume):
        """Set the alarm volume for the device."""
        data = {'volume': volume}
        endpoint = '/setup/assistant/alarms/volume'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        returnvalue = False
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.post(url,
                                                    json=data,
                                                    headers=HEADERS)
                if response.status == 200:
                    returnvalue = True
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to googledevices, %s', error)
        return returnvalue

    @property
    def alarms(self):
        """Return the alarms."""
        return self._alarms

    @property
    def alarm_volume(self):
        """Return the alarm volume."""
        return self._alarmvolume
