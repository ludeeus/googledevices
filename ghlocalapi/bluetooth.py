"""
Bluetooth handling on Google Home units.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import asyncio
import logging
import json
import socket
import time

import aiohttp
import async_timeout

from .const import API, HEADERS

_LOGGER = logging.getLogger(__name__)


class Bluetooth(object):
    """A class for Bluetooth scan ."""

    def __init__(self, loop, session, ipaddress):
        """Initialize the class."""
        self._loop = loop
        self._ipaddress = ipaddress
        self._session = session
        self._devices = []
        self._status = {}

    async def get_bluetooth_status(self):
        """Get the bluetooth status of the device."""
        endpoint = '/setup/bluetooth/status'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)
                self._status = await response.json()
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to GHLocalApi, %s', error)

    async def set_discovery_enabled(self):
        """Enable bluetooth discoverablility."""
        endpoint = '/setup/bluetooth/discovery'
        data = {"enable_discovery": True}
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.post(url,
                                                    headers=HEADERS,
                                                    data=json.dumps(data))
                _LOGGER.debug(response.status)
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to GHLocalApi, %s', error)

    async def scan_for_devices(self, sleep=5):
        """Scan for bluetooth devices."""
        endpoint = '/setup/bluetooth/scan'
        data = {"enable": True, "clear_results": True, "timeout": 5}
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        await self.set_discovery_enabled()
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.post(url,
                                                    headers=HEADERS,
                                                    data=json.dumps(data))
                _LOGGER.debug(response.status)
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to GHLocalApi, %s', error)
        time.sleep(sleep)

    async def get_scan_result(self):
        """Scan for bluetooth devices."""
        endpoint = '/setup/bluetooth/scan_results'
        url = API.format(ip=self._ipaddress, endpoint=endpoint)
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(url)
                self._devices = await response.json()
        except (asyncio.TimeoutError,
                aiohttp.ClientError, socket.gaierror) as error:
            _LOGGER.error('Error connecting to GHLocalApi, %s', error)

    @property
    def status(self):
        """Return the the bluetooth status of the device."""
        return self._status

    @property
    def devices(self):
        """Return the device info if any."""
        return self._devices
