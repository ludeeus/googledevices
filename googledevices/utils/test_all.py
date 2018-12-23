"""Test all connections."""
from googledevices.api.connect import Cast, Wifi
from googledevices.helpers import gdh_session, gdh_loop, gdh_sleep
from googledevices.utils.convert import format_json


TEST_HOST_CAST = '192.168.2.241'
TEST_HOST_WIFI = '192.168.2.1'
LOOP = gdh_loop()


async def test_all():  # pylint: disable=R0915
    """Test all."""
    print("Testing Cast.")

    print("Testing Cast - Alarm.")

    async with gdh_session() as session:
        print("Testing Cast - Alarm - get_alarms")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).alarm()
        test = await test_class.get_alarms()
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing Cast - Alarm - set_alarm_volume")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).alarm()
        test = await test_class.set_alarm_volume(0.6)
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing Cast - Alarm - get_alarm_volume")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).alarm()
        test = await test_class.get_alarm_volume()
        print(format_json(test))

    print("Testing Cast - Bluetooth.")

    async with gdh_session() as session:
        print("Testing Cast - Bluetooth - get_bluetooth_status")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).bluetooth()
        test = await test_class.get_bluetooth_status()
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing Cast - Bluetooth - set_discovery_enabled")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).bluetooth()
        test = await test_class.set_discovery_enabled()
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing Cast - Bluetooth - scan_for_devices")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).bluetooth()
        test = await test_class.scan_for_devices()
        print(format_json(test))
    async with gdh_session():
        await gdh_sleep(2)
    async with gdh_session() as session:
        print("Testing Cast - Bluetooth - get_scan_result")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).bluetooth()
        test = await test_class.get_scan_result()
        print(format_json(test))

    print("Testing Cast - Info.")

    async with gdh_session() as session:
        print("Testing Cast - Info - get_device_info")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).info()
        test = await test_class.get_device_info()
        print(format_json(test))

    print("Testing Cast - Settings.")

    async with gdh_session() as session:
        print("Testing Cast - Settings - control_notifications")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).settings()
        test = await test_class.control_notifications(True)
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing Cast - Settings - set_eureka_info")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).settings()
        data = {"settings": {"control_notifications": 2}}
        test = await test_class.set_eureka_info(data)
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing Cast - Settings - reboot")
        test_class = await Cast(TEST_HOST_CAST, LOOP, session).settings()
        test = await test_class.reboot()
        print(format_json(test))

    print("Testing WiFi.")

    print("Testing WiFi - Info.")

    async with gdh_session() as session:
        print("Testing WiFi - Info - get_host")
        test_class = await Wifi(TEST_HOST_WIFI, LOOP, session).info()
        test = await test_class.get_host()
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing WiFi - Info - get_host - with host not defined.")
        test_class = await Wifi(loop=LOOP, session=session).info()
        test = await test_class.get_host()
        print(format_json(test))
    async with gdh_session() as session:
        print("Testing WiFi - Info - get_wifi_info")
        test_class = await Wifi(TEST_HOST_WIFI, LOOP, session).info()
        test = await test_class.get_wifi_info()
        print(format_json(test))

    print("Testing WiFi - Clients.")

    async with gdh_session() as session:
        print("Testing WiFi - Clients - get_clients")
        test_class = await Wifi(TEST_HOST_WIFI, LOOP, session).clients()
        test = await test_class.get_clients()
        print(format_json(test))

    print("TESTS COMPLETE.")
LOOP.run_until_complete(test_all())
