"""CLI commands."""
import asyncio
import json
import click
import aiohttp


@click.group()
def device_info_group():
    """Click group."""
    pass


@click.group()
def scan_network_group():
    """Click group."""
    pass


@click.group()
def controll_notifications_group():
    """Click group."""
    pass


@click.group()
def reboot_group():
    """Click group."""
    pass


@device_info_group.command()
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


@scan_network_group.command()
@click.argument('subnet', required=1)
def scan_network(subnet):
    """Scan the entire subnet for Google devices."""
    from googledevices.scan import NetworkScan

    async def get_all_units():
        """Get device info from GH."""
        async with aiohttp.ClientSession() as session:
            googledevices = NetworkScan(LOOP, session)
            result = await googledevices.scan_for_units(subnet)
            print(json.dumps(result, indent=4, sort_keys=True))
    LOOP.run_until_complete(get_all_units())


@reboot_group.command()
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
CLI = click.CommandCollection(sources=[device_info_group,
                                       scan_network_group,
                                       reboot_group])
