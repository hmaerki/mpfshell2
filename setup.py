#!/usr/bin/env python
from setuptools import setup

from mp import version

setup(
    name="mpfshell2",
    version=version.FULL,
    description="A simple shell based file explorer for ESP8266 and WiPy "
    "Micropython devices.",
    author="Stefan Wendler, with extensions by Hans Maerki",
    author_email="sw@kaltpost.de, hans@maerki.com",
    url="https://github.com/hmaerki/mpfshell2",
    download_url=f"https://github.com/hmaerki/mpfshell2/archive/v{version.FULL}.zip",
    install_requires=["pyserial", "colorama", "websocket_client"],
    packages=["mp"],
    keywords=["micropython", "shell", "file transfer", "development"],
    classifiers=[],
    entry_points={"console_scripts": [
        "mpfshell=mp.mpfshell:main",
        "pyboard=mp.micropythonshell:main",
        "pyboard_query=mp.pyboard_query:main",
    ]},
)
