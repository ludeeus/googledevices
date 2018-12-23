"""Googledevices helpers.

All methods are prefixed with 'gdh_' for (GoogleDevicesHelpers).
"""


def gdh_loop():
    """Asyncio loop."""
    from asyncio import get_event_loop
    return get_event_loop()


def gdh_session():
    """Aiohttp clientsession."""
    from aiohttp import ClientSession
    return ClientSession()


async def gdh_sleep(seconds=5):
    """Asyncio sleep."""
    from asyncio import sleep
    await sleep(seconds)


async def gdh_request(host, port=None, endpoint=None, json=True,
                      session=None, loop=None, headers=None,
                      data=None, json_data=None, params=None, method='get'):
    """Web request."""
    import asyncio
    import aiohttp
    import async_timeout
    from socket import gaierror
    from googledevices.utils.const import API
    import googledevices.utils.log as log

    if port is not None:
        port = ":{port}".format(port=port)
    else:
        port = ""
    url = API.format(host=host, port=port, endpoint=endpoint)
    result = None

    if session is None:
        session = gdh_session()
    if loop is None:
        loop = gdh_loop()
    try:
        async with async_timeout.timeout(8, loop=loop):
            if method == 'post':
                async with session as session:
                    webrequest = await session.post(url, json=json_data,
                                                    data=data, params=params,
                                                    headers=headers)
            else:
                async with session as session:
                    webrequest = await session.get(url, json=json_data,
                                                   data=data, params=params,
                                                   headers=headers)
            if json:
                result = await webrequest.json()
            else:
                result = webrequest
    except (TypeError, KeyError, IndexError) as error:
        msg = "Error parsing information - {}".format(error)
        log.error(msg)
    except (asyncio.TimeoutError, aiohttp.ClientError, gaierror,
            asyncio.CancelledError) as error:
        msg = "{} - {}".format(url, error)
        log.error(msg)
    except Exception as error:  # pylint: disable=W0703
        log.error(error)
    return result
