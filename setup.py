"""Setup configuration."""
import setuptools

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="googledevices",
    version="0.5.0",
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description=LONG,
    install_requires=['aiohttp', 'async_timeout', 'click', 'netifaces'],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/googledevices",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'googledevices = googledevices.cli.commands:CLI'
        ]
    },
)
