"""CLI commands."""
import asyncio
import json
import click
import aiohttp


@click.group()
def commands():
    """Click group."""


@commands.command()
@click.argument('ip_address', required=1)
def device_info(ip_address):
    """Get information about a Google device on your network."""
    from googledevices.api.device_info import DeviceInfo

    async def get_device_info():
        """Get device info."""
        async with aiohttp.ClientSession() as session:
            googledevices = DeviceInfo(LOOP, session, ip_address)
            await googledevices.get_device_info()
            print(json.dumps(googledevices.device_info,
                             indent=4, sort_keys=True))
    LOOP.run_until_complete(get_device_info())


@commands.command()
@click.argument('ip_address', required=1)
def get_bluetooth_devices(ip_address):
    """Get bluetooth devices from a unit."""
    from googledevices.api.bluetooth import Bluetooth

    async def bluetooth_scan():
        """Get nearby bluetooth devices."""
        async with aiohttp.ClientSession() as session:
            googledevices = Bluetooth(LOOP, session, ip_address)
            await googledevices.scan_for_devices()
            await googledevices.get_scan_result()
            print(json.dumps(googledevices.devices, indent=4, sort_keys=True))
    LOOP.run_until_complete(bluetooth_scan())


@commands.command()
@click.option('--subnet', type=str, default=None, help="Format 0.0.0.0/00")
def get_all_devices(subnet):
    """Get information about all devices on your network."""
    from googledevices.api.bluetooth import Bluetooth
    from googledevices.utils.scan import NetworkScan
    from googledevices.api.device_info import DeviceInfo

    async def bluetooth_scan():
        """Get devices from all GH units on the network."""
        if not subnet:
            import netifaces
            gateway = netifaces.gateways().get('default', {})
            ipscope = gateway.get(netifaces.AF_INET, ())[0][:-1] + '0/24'
        else:
            ipscope = subnet
        devices = {}
        async with aiohttp.ClientSession() as session:
            googledevices = NetworkScan(LOOP, session)
            result = await googledevices.scan_for_units(ipscope)
        for host in result:
            if host['assistant']:
                async with aiohttp.ClientSession() as session:
                    googledevices = DeviceInfo(LOOP, session, host['host'])
                    await googledevices.get_device_info()
                    ghname = googledevices.device_info.get('name')
                async with aiohttp.ClientSession() as session:
                    googledevices = Bluetooth(LOOP, session, host['host'])
                    await googledevices.scan_for_devices_multi_run()
                    await googledevices.get_scan_result()
                    for device in googledevices.devices:
                        mac = device['mac_address']
                        if not devices.get(mac, False):
                            # New device
                            devices[mac] = {}
                            devices[mac]['rssi'] = device['rssi']
                            devices[mac]['ghunit'] = ghname
                        elif devices[mac]['rssi'] < device['rssi']:
                            # Better RSSI value on this device
                            devices[mac]['rssi'] = device['rssi']
                            devices[mac]['ghunit'] = ghname
        print(json.dumps(devices, indent=4, sort_keys=True))
    LOOP.run_until_complete(bluetooth_scan())


@commands.command()
@click.option('--network', '-N', type=str, default=None,
              help="The network you want to scan\
              in this format '192.168.1.0/24'.")
@click.option('--feature', '-F', type=str, default=None,
              help="Filter discovery result to\
              units that contain these feature.")
def scan_network(network, feature):
    """Scan the entire subnet for Google devices."""
    from googledevices.utils.scan import NetworkScan

    async def get_all_units():
        """Get device info for all Google devices."""
        all_devices = []
        if network is None:
            import netifaces
            gateway = netifaces.gateways().get('default', {})
            subnet = gateway.get(netifaces.AF_INET, ())[0][:-1] + '0/24'
        else:
            subnet = network
        async with aiohttp.ClientSession() as session:
            googledevices = NetworkScan(LOOP, session)
            result = await googledevices.scan_for_units(subnet)
            if feature:
                for unit in result:
                    if unit[feature]:
                        all_devices.append(unit)
            else:
                all_devices = result
            print(json.dumps(all_devices, indent=4, sort_keys=True))
    LOOP.run_until_complete(get_all_units())


@commands.command()
@click.argument('ip_address', required=1)
def reboot(ip_address):
    """Reboot a Google device."""
    from googledevices.api.device_settings import DeviceSettings

    async def reboot_device():
        """Reboot a Google Home unit."""
        async with aiohttp.ClientSession() as session:
            googledevices = DeviceSettings(LOOP, session, ip_address)
            await googledevices.reboot()
    LOOP.run_until_complete(reboot_device())


@commands.command()
@click.option('--system', '-S', is_flag=True, help="Print more output.")
def info(system):
    """Get information about this package."""
    import googledevices.utils.const as package
    print("Projectname:  ", package.NAME)
    print("Version:      ", package.VERSION)
    print("GitHub link:  ", package.URLS.get('github'))
    print("PyPi link:    ", package.URLS.get('pypi'))
    print("Maintainers:")
    for maintainer in package.MAINTAINERS:
        print("    ", maintainer.get('name'),
              "(", maintainer.get('github'), ")")
    print("")
    if system:
        import platform
        print("")
        print("System:          ", platform.system())
        print("Version:         ", platform.version())
        print("Python version:  ", platform.python_version())


@commands.command()
@click.argument('ip_address', required=1)
@click.option('--test', '-T', type=str, required=1)
@click.option('--timeout', type=int)
def debug(ip_address, test, timeout=30):
    """Get information about this package."""
    from googledevices.utils.debug import Debug

    async def connectivity():
        """Reboot a Google Home unit."""
        async with aiohttp.ClientSession() as session:
            googledevices = Debug(LOOP, session, ip_address)
            await googledevices.connectivity(timeout)
    if test == 'connectivity':
        LOOP.run_until_complete(connectivity())


LOOP = asyncio.get_event_loop()
CLI = click.CommandCollection(sources=[commands])
