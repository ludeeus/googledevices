"""
Tools to debug with.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import socket
import asyncio
import time
from googledevices.utils.const import PORT


class Debug(object):
    """A class for debug."""

    def __init__(self, loop, session, ip_address):
        """Initialize the class."""
        self._loop = loop
        self._session = session
        self._ip_address = ip_address

    async def connectivity(self, timeout):
        """Test connectivity."""
        host = str(self._ip_address)
        stop_timeout = time.time() + timeout
        while True:  # Yes I know this is bad...
            if time.time() > stop_timeout:
                try:
                    sock = socket.socket()
                    sock.settimeout(0.02)
                    scan_result = sock.connect((host, PORT))
                    sock.close()
                except socket.error:
                    scan_result = 1
                now = time.time()
                if scan_result is None:
                    print(now, "- OK")
                else:
                    print(now, "- ERROR")
                asyncio.sleep(1)
