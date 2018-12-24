[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [CLASSES][classes] | [**METHODS**][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

## [Cast](https://ludeeus.github.io/googledevices/platforms#cast) - [Assistant](https://ludeeus.github.io/googledevices/classes/cast/assistant) - [`set_night_mode_params`](https://ludeeus.github.io/googledevices/methods/cast/assistant/set_night_mode_params)

This takes one required parameter.  
This **needs** to be formated like this:

```json
{
  "enabled": false,
  "do_not_disturb": true,
  "led_brightness": 0.44999998807907104,
  "volume": 0.46000000834465027,
  "demo_to_user": true,
  "windows": [
    {
      "length_hours": 8,
      "days": [
        0,
        1,
        2,
        3,
        4,
        5,
        6
      ],
      "start_hour": 22
    }
  ]
}
```

Only add the keys you want to send, you can also just send `{}`.

Sample usage:

```python
from googledevices.api.connect import Cast
from googledevices.helpers import gdh_session, gdh_loop
from googledevices.utils.convert import format_json

CAST_HOST = '192.168.2.241'
LOOP = gdh_loop()

async def sample():
    """Sample usage."""
    async with gdh_session() as session:
        sample_class = await Cast(CAST_HOST, LOOP, session).assistant()
        data = {}
        test = await sample_class.set_night_mode_params(data)
        print(format_json(test))
LOOP.run_until_complete(sample())
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