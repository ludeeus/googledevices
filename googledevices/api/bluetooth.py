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

from googledevices.utils.const import API, HEADERS

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
            _LOGGER.error('Error connecting to googledevices, %s', error)

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
            _LOGGER.error('Error connecting to googledevices, %s', error)

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
            _LOGGER.error('Error connecting to googledevices, %s', error)
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
            _LOGGER.error('Error connecting to googledevices, %s', error)

    async def scan_for_devices_multi_run(self, runs=2):
        """Scan for devices multiple times."""
        run = 1
        master = {}
        while run < runs + 1:
            await self.scan_for_devices()
            await self.get_scan_result()
            if master is None:
                for device in self._devices:
                    mac = device.get('mac_address')
                    master[mac] = {}
                    master[mac]['rssi'] = device.get('rssi')
                    master[mac]['device_class'] = device.get('device_class')
                    master[mac]['name'] = device.get('name')
                    master[mac]['device_type'] = device.get('device_type')
                    master[mac]['count'] = 1
            else:
                for device in self._devices:
                    mac = device.get('mac_address')
                    if master.get(mac, False):
                        master[mac]['rssi'] = device.get('rssi')
                        master[mac]['count'] = str(1 + 1)
                    else:
                        master[mac] = {}
                        master[mac]['rssi'] = device.get('rssi')
                        device_class = device.get('device_class')
                        master[mac]['device_class'] = device_class
                        master[mac]['name'] = device.get('name')
                        master[mac]['device_type'] = device.get('device_type')
                        master[mac]['count'] = 1
            run = run + 1
            result = []
            for device in master:
                if int(master.get(device, {}).get('count')) > 1:
                    result.append(master[device])
        self._devices = result

    @property
    def status(self):
        """Return the the bluetooth status of the device."""
        return self._status

    @property
    def devices(self):
        """Return the device info if any."""
        return self._devices
