"""Initialize logging."""
import logging
from googledevices.utils.const import NAME

LOG = logging.getLogger(NAME)


async def error(message):
    """Error log."""
    LOG.error(message)


async def info(message):
    """Info log."""
    LOG.info(message)


async def debug(message):
    """Info log."""
    LOG.debug(message)
