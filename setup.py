#coding=utf-8

#Created by Alfred Jiang 20160523

from setuptools import setup

APP = ['auto_ssp_gui.py']
DATA_FILES = ['auto_ssp_key.icns']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleIconFile': 'auto_ssp_key.icns',
        'CFBundleName': 'AutoSSP',
        'CFBundleDisplayName': 'AutoSSP',
        'CFBundleGetInfoString': "Alfred Jiang",
        'CFBundleIdentifier': "com.alfredjiang.autossp",
        'CFBundleVersion': "0.0.1",
        'CFBundleShortVersionString': "0.0.1",
        'NSHumanReadableCopyright': u"Copyright © 2016, Alfred Jiang, All Rights Reserved"

    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)