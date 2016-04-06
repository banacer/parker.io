# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Parker.io',
    version='0.0.1',
    description=' A tool to find parking for users using sensors and ML',
    long_description=readme,
    author='Nacer Khalil',
    author_email='nacerkhalil@gmil.com',
    url='https://github.com/banacer/parker.io',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

