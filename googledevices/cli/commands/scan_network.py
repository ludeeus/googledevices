"""Scan the entire subnet for Google devices."""
from json import dumps
from aiohttp import ClientSession


def scan_network(loop, network, feature):
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
        async with ClientSession() as session:
            googledevices = NetworkScan(loop, session)
            result = await googledevices.scan_for_units(subnet)
            if feature:
                for unit in result:
                    if unit[feature]:
                        all_devices.append(unit)
            else:
                all_devices = result
            print(dumps(all_devices, indent=4, sort_keys=True))
    loop.run_until_complete(get_all_units())
