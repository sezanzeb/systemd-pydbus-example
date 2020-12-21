#!/usr/bin/python3
# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name='systemd-pydbus-example',
    version='1.0.0',
    description='Example setup for a pydbus server controllable via systemctl',
    url='https://github.com/sezanzeb/systemd-pydbus-example',
    license='unlicense',
    data_files=[
        ('/usr/lib/systemd/system', ['data/systemd-pydbus-example.service']),
        ('/etc/dbus-1/system.d/', ['data/example.foo.bar.conf']),
        ('/usr/bin/', ['bin/systemd-pydbus-example-client']),
        ('/usr/bin/', ['bin/systemd-pydbus-example-server']),
    ],
    install_requires=[
        'setuptools',
        'pydbus'
    ],
)
