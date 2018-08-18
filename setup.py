#!/usr/bin/python3

from distutils.core import setup

setup(
    name='Screen Time',
    version='1.1',
    author='Kyle Corry',
    description='View your computer usage',
    url='https://github.com/kylecorry31/ScreenTimen',
    license='MIT',
    scripts=['screen_time/screen_time', 'screen-time-daemon'],
    packages=['screen_time'],
    data_files=[
        ('share/metainfo', ['data/screen_time.appdata.xml']),
        ('share/icons', ['data/screen_time.png']),
        ('share/applications', ['data/screen_time.desktop']),
    ],
)