[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [CLASSES][classes] | [**METHODS**][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

## [Cast](https://ludeeus.github.io/googledevices/platforms#wifi) - [Assistant](https://ludeeus.github.io/googledevices/classes/wifi/clients) - [`get_clients`](https://ludeeus.github.io/googledevices/methods/wifi/clients/get_clients)

Sample usage:

```python
from googledevices.api.connect import Wifi
from googledevices.helpers import gdh_session, gdh_loop
from googledevices.utils.convert import format_json

WIFI_HOST = '192.168.2.1'
LOOP = gdh_loop()

async def sample():
    """Sample usage."""
    async with gdh_session() as session:
        test_class = await Wifi(WIFI_HOST, LOOP, session).clients()
        test = await test_class.get_clients()
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