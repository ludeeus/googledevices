[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [**CLASSES**][classes] | [METHODS][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

This class handles methods that are nested under the `assistant` endpoint.

## Methods for the `Assistant` class.

- [set_night_mode_params](https://ludeeus.github.io/googledevices/methods/cast/assistant/set_night_mode_params)
- [notifications_enabled](https://ludeeus.github.io/googledevices/methods/cast/assistant/notifications_enabled)
- [set_accessibility](https://ludeeus.github.io/googledevices/methods/cast/assistant/set_accessibility)
- [delete_alarms](https://ludeeus.github.io/googledevices/methods/cast/assistant/delete_alarms)
- [set_equalizer](https://ludeeus.github.io/googledevices/methods/cast/assistant/set_equalizer)
- [get_alarms](https://ludeeus.github.io/googledevices/methods/cast/assistant/get_alarms)
- [get_alarm_volume](https://ludeeus.github.io/googledevices/methods/cast/assistant/get_alarm_volume)
- [set_alarm_volume](https://ludeeus.github.io/googledevices/methods/cast/assistant/set_alarm_volume)

## Properties for the `Assistant` class.

- `alarms` Returns active alarms and timers. _You need to run the [get_alarms](https://ludeeus.github.io/googledevices/methods/cast/assistant/get_alarms) method before this get populated._
- `alarm_volume` Returns the current alarm volume. _You need to run the [get_alarm_volume](https://ludeeus.github.io/googledevices/methods/cast/assistant/get_alarm_volume) method before this get populated._

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