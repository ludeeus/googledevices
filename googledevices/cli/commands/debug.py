"""Get debug information."""
from aiohttp import ClientSession


def debug(loop, ip_address, test, timeout):
    """Get debug information."""
    from googledevices.utils.debug import Debug

    async def connectivity():
        """Test connectivity a Google Home unit."""
        async with ClientSession() as session:
            googledevices = Debug(loop, session, ip_address)
            await googledevices.connectivity(timeout)

    if test == 'connectivity':
        loop.run_until_complete(connectivity())
