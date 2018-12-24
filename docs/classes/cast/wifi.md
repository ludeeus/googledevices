[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [**CLASSES**][classes] | [METHODS][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

This class handles methods that are nested under the `wifi` endpoint.

## Methods for the `Wifi` class.

- [forget_network](https://ludeeus.github.io/googledevices/methods/cast/wifi/forget_network)
- [get_configured_networks](https://ludeeus.github.io/googledevices/methods/cast/wifi/get_configured_networks)
- [get_wifi_scan_result](https://ludeeus.github.io/googledevices/methods/cast/wifi/get_wifi_scan_result)
- [scan_for_wifi](https://ludeeus.github.io/googledevices/methods/cast/wifi/scan_for_wifi)

## Properties for the `Wifi` class.

- `configured_networks` Return the configured networks of the device. _You need to run the [get_configured_networks](https://ludeeus.github.io/googledevices/methods/cast/wifi/get_configured_networks) method before this get populated._
- `nearby_networks` Return the nearby networks of the device. _You need to run the [get_wifi_scan_result](https://ludeeus.github.io/googledevices/methods/cast/wifi/get_wifi_scan_result) method before this get populated._

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