"""CLI commands."""
from asyncio import get_event_loop
import click


@click.group()
async def commands():
    """Click group."""


@commands.command('device-info')
@click.argument('ip_address', required=1)
def device_info(ip_address):
    """Get information about a Google device on your network."""
    import googledevices.cli.commands.device_info as command
    command.device_info(LOOP, ip_address)


@commands.command('get-bluetooth-devices')
@click.argument('ip_address', required=1)
def get_bluetooth_devices(ip_address):
    """Get bluetooth devices from a unit."""
    import googledevices.cli.commands.bluetooth_devices as command
    command.get_bluetooth_devices(LOOP, ip_address)


@commands.command('get-all-devices')
@click.option('--subnet', type=str, default=None, help="Format 0.0.0.0/00")
def get_all_devices(subnet):
    """Get information about all devices on your network."""
    import googledevices.cli.commands.all_devices as command
    command.get_all_devices(LOOP, subnet)


@commands.command('scan-network')
@click.option('--network', '-N', type=str, default=None,
              help="The network you want to scan\
              in this format '192.168.1.0/24'.")
@click.option('--feature', '-F', type=str, default=None,
              help="Filter discovery result to\
              units that contain these feature.")
def scan_network(network, feature):
    """Scan the entire subnet for Google devices."""
    import googledevices.cli.commands.scan_network as command
    command.scan_network(LOOP, network, feature)


@commands.command('reboot')
@click.argument('ip_address', required=1)
def reboot(ip_address):
    """Reboot a Google device."""
    import googledevices.cli.commands.reboot as command
    command.reboot(LOOP, ip_address)


@commands.command('googlewifi-info')
@click.argument('ip_address', required=0)
def get_wifi_info(ip_address):
    """Reboot a Google device."""
    import googledevices.cli.commands.googlewifi as command
    command.get_wifi_info(LOOP, ip_address)


@commands.command('info')
@click.option('--system', '-S', is_flag=True, help="Print more output.")
def info(system):
    """Get information about this package."""
    import googledevices.cli.commands.info as command
    command.info(system)


@commands.command('debug')
@click.argument('ip_address', required=1)
@click.option('--test', '-T', type=str, required=1)
@click.option('--timeout', type=int)
def debug(ip_address, test, timeout=30):
    """Get debug information."""
    import googledevices.cli.commands.debug as command
    command.debug(LOOP, ip_address, test, timeout)


@commands.command('alarm-volume')
@click.argument('ip_address', required=1)
@click.option('--mode', '-M', type=str, required=1, help="'get' or 'set'")
@click.option('--volume', '-V', type=int)
def alarm_volume(ip_address, mode, volume=None):
    """Get or set alarm volume."""
    import googledevices.cli.commands.alarm_volume as command
    command.alarm_volume(LOOP, ip_address, mode, volume)


LOOP = get_event_loop()
CLI = click.CommandCollection(sources=[commands])
