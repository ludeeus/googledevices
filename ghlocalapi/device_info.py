"""
Get device information for the unit.

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


class DeviceInfo(object):
    """A class for device info."""

    def __init__(self, loop, session, ipaddress):
        """Initialize the class."""
        self._loop = loop
        self._ipaddress = ipaddress
        self._session = session
        self._device_info = {}

    async def get_device_info(self):
        """Get the bluetooth status of the device."""
        endpoint = '/setup/eureka_info'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        params = "params=version,audio,name,build_info,detail,device_info, \
                  net,wifi,setup,settings,opt_in,opencast,multizone,proxy, \
                  night_mode_params,user_eq,room_equalizer&options=detail"
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url, params=params)
                self._device_info = await response.json()
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to GHLocalApi, %s', error)

    @property
    def device_info(self):
        """Return the device info if any."""
        return self._device_info
