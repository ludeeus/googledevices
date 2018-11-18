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

from .const import API

_LOGGER = logging.getLogger(__name__)


class Alarms(object):
    """A class for getting the alarms from a Google Home."""

    def __init__(self, loop, session, ipaddress):
        """Initialize the class."""
        self._loop = loop
        self._ipaddress = ipaddress
        self._session = session
        self._alarms = []

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
            _LOGGER.error('Error connecting to GHLocalApi, %s', error)

    @property
    def alarms(self):
        """Return the alarms."""
        return self._alarms
