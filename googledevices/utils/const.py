"""Constants."""
API = 'http://{ip}:8008{endpoint}'
DEFAULT_DEVICE_NAME = 'GoogleDevice'
GOOGLE_WIFI_API = 'http://{ip}/api/v1/{endpoint}'
HEADERS = {
    'Content-Type': 'application/json',
    'Host': 'localhost'
    }
PORT = 8008
WIFI_HOSTS = ['192.168.86.1', 'testwifi.here', 'onhub.here']

# Setup information:
VERSION = '0.6.0'
NAME = 'googledevices'
URLS = {
    'github': 'https://github.com/ludeeus/googledevices',
    'pypi': 'https://pypi.org/project/googledevices'
}
AUTHOR = {'name': 'Joakim Sorensen', 'email': 'ludeeus@gmail.com'}
MAINTAINERS = [
    {
        'name': 'ludeeus',
        'github': 'https://github.com/ludeeus',
        'email': AUTHOR.get('email')
    },
    {
        'name': 'eliseomartelli',
        'github': 'https://github.com/eliseomartelli',
        'email': 'me@eliseomartelli.it'
    }
]
REQUIREMENTS = ['aiohttp', 'async_timeout', 'click', 'netifaces']
CLASSIFIERS = ("Programming Language :: Python :: 3",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent")
ENTRY_POINTS = {
    'console_scripts': [
        'googledevices = googledevices.cli.cli:CLI'
    ]
}
