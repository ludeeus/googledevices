"""Setup configuration."""
import setuptools
import googledevices.utils.const as package

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name=package.NAME,
    version=package.VERSION,
    author=package.AUTHOR.get('name'),
    author_email=package.AUTHOR.get('email'),
    description=package.DESCRIPTION,
    long_description=LONG,
    install_requires=package.REQUIREMENTS,
    long_description_content_type="text/markdown",
    url=package.URLS.get('github'),
    packages=setuptools.find_packages(),
    classifiers=package.CLASSIFIERS,
    entry_points=package.ENTRY_POINTS
)
