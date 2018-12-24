[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [CLASSES][classes] | [METHODS][methods] | [FUNCTIONS][functions] | [**CLI**][cli]

***

This package comes with a CLI.  

```bash
Usage: googledevices [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  alarm-volume           Get or set alarm volume.
  debug                  Get debug information.
  device-info            Get information about a Google device on your...
  get-all-devices        Get information about all devices on your network.
  get-bluetooth-devices  Get bluetooth devices from a unit.
  googlewifi-clients     Get devices from google wifi.
  googlewifi-info        Get information about google wifi.
  info                   Get information about this package.
  reboot                 Reboot a Google device.
  scan-network           Scan the entire subnet for Google devices.
```

Sample usage of the CLI:

```bash
username@hostname:~$ googledevices scan-network
[
    {
        "assistant": false,
        "bluetooth": false,
        "host": "192.168.2.136",
        "model": "Chromecast Ultra",
        "name": "ChromeCast ULTRA"
    },
    {
        "assistant": false,
        "bluetooth": false,
        "host": "192.168.2.188",
        "model": "Chromecast",
        "name": "Chrome Cast"
    },
    {
        "assistant": true,
        "bluetooth": true,
        "host": "192.168.2.234",
        "model": "Google Home Mini",
        "name": "Living Room"
    }
]
```

<!-- menu -->
[travis]: https://travis-ci.com/ludeeus/googledevices
[travis_status]: https://travis-ci.com/ludeeus/googledevices.svg?branch=master
[pypi]:https://pypi.org/project/googledevices/
[pypi_badge]: https://badge.fury.io/py/googledevices.svg
[home]: https://ludeeus.github.io/googledevices
[platforms]: https://ludeeus.github.io/googledevices/platforms
[classes]: https://ludeeus.github.io/googledevices/classes
[methods]: https://ludeeus.github.io/googledevices/methods
[functions]: https://ludeeus.github.io/googledevices/functions
[cli]: https://ludeeus.github.io/googledevices/cli