"""
Convert/restructure data sets.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""


def get_device_type(device_type=0):
    """Return the device type from a device_type list."""
    device_types = {
        0: "Unknown",
        1: "Classic - BR/EDR devices",
        2: "Low Energy - LE-only",
        3: "Dual Mode - BR/EDR/LE"
    }
    if device_type in [0, 1, 2, 3]:
        return_value = device_types[device_type]
    else:
        return_value = device_types[0]
    return return_value
