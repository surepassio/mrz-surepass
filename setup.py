#!/usr/bin/python3
# -*- coding: UTF8 -*-

from setuptools import setup
from sys import version_info, exit
from os import path
from mrz import __version__ as version

if version_info < (3, 6):
    RED = "\33[31m"
    END = "\033[0m"
    print("%s%s%s" % (RED, "MRZ does not work on Python version < 3.6", END))
    print("Your version is: %d.%d.%d" % (version_info.major, version_info.minor, version_info.micro))
    exit(1)

parent = path.abspath(path.dirname(__file__))

with open(path.join(parent, "README.md"), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name="mrz-surepass",
    version=version,
    description="Machine readable zone generator and checker for passports, visas, id cards and other travel documents",
    license="GPLv3",
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Rishabh Chauhan',
    author_email='rc@surepass.io',
    url="https://github.com/surepassio/mrz-surepass",
    keywords="mrz passports visas id cards td1 td2 td3 mrva mrvb icao",
    packages=["mrz", "mrz.base", "mrz.checker", "mrz.generator", "mrz.generator.dictionaries",
              "mrz.special_cases.checker", "mrz.special_cases.generator"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security"
    ]
)
