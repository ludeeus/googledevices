[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [**CLASSES**][classes] | [METHODS][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

This class handles methods that are nested under the `bluetooth` endpoint.

## Methods for the `Bluetooth` class.

- [forget_paired_device](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/forget_paired_device)
- [get_bluetooth_status](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/get_bluetooth_status)
- [get_paired_devices](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/get_paired_devices)
- [get_scan_result](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/get_scan_result)
- [pair_with_mac](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/pair_with_mac)
- [scan_for_devices](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/scan_for_devices)
- [set_discovery_enabled](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/set_discovery_enabled)

## Properties for the `Bluetooth` class.

- `status` Return the the bluetooth status of the device. _You need to run the [get_bluetooth_status](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/get_bluetooth_status) method before this get populated._
- `devices` Return the devices if any. _You need to run the [get_scan_result](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/get_scan_result) method before this get populated._
- `paired_devices` Return paired devices if any. _You need to run the [get_paired_devices](https://ludeeus.github.io/googledevices/methods/cast/bluetooth/get_paired_devices) method before this get populated._

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