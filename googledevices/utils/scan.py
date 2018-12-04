"""
Get GH devices on the local network.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import socket
import ipaddress
from googledevices.api.device_info import DeviceInfo
from googledevices.utils.const import PORT


class NetworkScan(object):
    """A class nettwork scan."""

    def __init__(self, loop, session):
        """Initialize the class."""
        self._loop = loop
        self._session = session

    async def scan_for_units(self, iprange):
        """Scan local network for GH units."""
        units = []
        for ip_address in ipaddress.IPv4Network(iprange):
            sock = socket.socket()
            sock.settimeout(0.05)
            host = str(ip_address)
            try:
                scan_result = sock.connect((host, PORT))
            except socket.error:
                scan_result = 1
            if scan_result is None:
                googledevices = DeviceInfo(self._loop, self._session, host)
                await googledevices.get_device_info()
                data = googledevices.device_info
                if data is not None:
                    info = data.get('device_info', {})
                    cap = info.get('capabilities', {})
                    units.append({
                        'host': host,
                        'name': data.get('name'),
                        'model': info.get('model_name'),
                        'assistant': cap.get('assistant_supported', False),
                        'bluetooth': cap.get('bluetooth_supported', False)
                    })
            sock.close()
        return units
