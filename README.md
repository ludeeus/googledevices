# googledevices [![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi]

_API wrapper for Google devices written in Python._

This Python package is based of the works of [rithvikvibhu/GHLocalApi][GHLocalApi]

## Install

```bash
pip install googledevices
```

Look at the files in the `examples` directory for usage examples.

This package also comes with a CLI.  
To start using that run `googledevices --help` after installation.

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

### Maintainers

- [ludeeus][ludeeus]
- [eliseomartelli][eliseomartelli]

#### Notice

_This is not affiliated, associated, authorized, endorsed by, or in any way officially connected with [Alphabet][alphabet], or any of its subsidiaries or its affiliates. The name "Google" as well as related names, marks, emblems and images are registered trademarks of [Alphabet][alphabet]._

[alphabet]: https://abc.xyz/
[eliseomartelli]: https://github.com/eliseomartelli
[GHLocalApi]: https://github.com/rithvikvibhu/GHLocalApi
[ludeeus]: https://github.com/ludeeus
[travis]: https://travis-ci.com/ludeeus/googledevices
[travis_status]: https://travis-ci.com/ludeeus/googledevices.svg?branch=master
[pypi]:https://pypi.org/project/googledevices/
[pypi_badge]: https://badge.fury.io/py/googledevices.svg