#!/usr/bin/env python3
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='utcformatter',
    version='0.1.0',
    description='logging.Formatter with UTC timezone',
    long_description=long_description,
    url='https://github.com/czchen/utcformatter',
    author='ChangZhuo Chen',
    author_email='czchen@czchen.org',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='logging',
    packages=find_packages()
)
