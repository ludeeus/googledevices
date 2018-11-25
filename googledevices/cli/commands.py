"""CLI commands."""
import asyncio
import json
import click
import aiohttp


@click.group()
def commands():
    """Click group."""
    pass


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


LOOP = asyncio.get_event_loop()
CLI = click.CommandCollection(sources=[commands])
