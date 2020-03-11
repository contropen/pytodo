#!/usr/bin/python

from setuptools import find_packages


import os
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

from setuptools import setup

setup(
    name="pytodo",
    version='0.1',
    author="Mugdha Dalal",
    author_email="mugdhadalal@gmail.com",
    url="https://github.com/contropen/pytodo.git",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=['click>=0.1'],
    entry_points={"console_scripts": ["pytodo=pytodo:main"]},
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["pytodo"]),
    flake8={"max_line_length": 100},
) 
