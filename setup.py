#coding=utf-8

#Created by Alfred Jiang 20160523

from setuptools import setup

APP = ['auto_ssp_gui.py']
DATA_FILES = ['auto_ssp.py','base64_codec.py']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)