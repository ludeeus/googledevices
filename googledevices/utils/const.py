"""Constants."""
API = 'http://{ip}:8008{endpoint}'
HEADERS = {'Content-Type': 'application/json'}
PORT = 8008

# Setup information:
VERSION = '0.5.0'
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
        'googledevices = googledevices.cli.commands:CLI'
    ]
}
