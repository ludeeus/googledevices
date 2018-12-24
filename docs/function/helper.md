[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [CLASSES][classes] | [METHODS][methods] | [**FUNCTIONS**][functions] | [CLI][cli]

***

## [Functions](https://ludeeus.github.io/googledevices/functions) Helper functions

### gdh_loop

This only returns `get_event_loop()` from `asyncio`.

```python
# Sample usage
from googledevices.helpers import gdh_loop
loop = gdh_loop()
```

### gdh_session

This only returns `ClientSession()` from `aiohttp`.

```python
# Sample usage
from googledevices.helpers import gdh_session
session = gdh_session()
```

### gdh_sleep

This uses `sleep` from `asyncio` with an optional param for the number of seconds, defaults to 5.

```python
# Sample usage
from googledevices.helpers import gdh_sleep
await gdh_sleep(5)
```

### gdh_request

This has a lot of possible params.

param | required | description
-- | -- | --
host | True | Hostname or IP address
port | False | Port
endpoint | False | endpoint
json | False | Bool for if the returned response from the server are JSON or not.
session | False | Session
loop | False | Loop
headers | False | Request headers
data | False | Data to send with the request
json_data | False | JSON formated data to send with the request
params | False | Params to send with the request
method | False | `get` or `post`, defaults to `get`

```python
# Sample usage
from googledevices.helpers import gdh_request
request = await gdh_request('192.168.2.1')
print(request)
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