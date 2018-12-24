[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [**CLASSES**][classes] | [METHODS][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

This class handles methods that are nested under the `info` endpoint.

## Methods for the `Info` class.

- [get_app_device_id](https://ludeeus.github.io/googledevices/methods/cast/info/get_app_device_id)
- [get_device_info](https://ludeeus.github.io/googledevices/methods/cast/info/get_device_info)
- [get_locales](https://ludeeus.github.io/googledevices/methods/cast/info/get_locales)
- [get_offer](https://ludeeus.github.io/googledevices/methods/cast/info/get_offer)
- [get_timezones](https://ludeeus.github.io/googledevices/methods/cast/info/get_timezones)
- [speedtest](https://ludeeus.github.io/googledevices/methods/cast/info/speedtest)

## Properties for the `Info` class.

- `offer` Return the offer token. _You need to run the [get_offer](https://ludeeus.github.io/googledevices/methods/cast/info/get_offer) method before this get populated._
- `timezones` Return supported timezones. _You need to run the [get_timezones](https://ludeeus.github.io/googledevices/methods/cast/info/get_timezones) method before this get populated._
- `locales` Return supported locales. _You need to run the [get_locales](https://ludeeus.github.io/googledevices/methods/cast/info/get_locales) method before this get populated._
- `app_device_id` Return app_device_id. _You need to run the [get_app_device_id](https://ludeeus.github.io/googledevices/methods/cast/info/get_app_device_id) method before this get populated._
- `device_info` Return the device info if any. _You need to run the [get_device_info](https://ludeeus.github.io/googledevices/methods/cast/info/get_device_info) method before this get populated._
- `name` Return the device name. _You need to run the [get_device_info](https://ludeeus.github.io/googledevices/methods/cast/info/get_device_info) method before this get populated._

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