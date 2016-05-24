# AutoSSP

An easy way to fetch free account configuration of Shadowsocks.

*Written in Python and Shadowsocks for Mac only.*

## Usage

###### 1. By AutoSSP.app 

* Download `AutoSSP.app` from [Here](https://github.com/viktyz/AutoSSP/releases/download/0.0.1/AutoSSP.zip)
* Double click `AutoSSP.app` to open SSP.
* Select any service from the drop list of SSP.
* Then the configuration of the Shadowsocks will be updated.

###### 2. By Terminal with auto_ssp.py

* Save [auto_ssp.py](https://github.com/viktyz/AutoSSP/blob/master/auto_ssp.py) to your mac.
* Execute the following command in your Terminal
```shell 
python auto_ssp.py
```
* Then the configuration of the Shadowsocks will be updated.

## Required

If your want to build `AutoSSP.app` by source code of AutoSSP. The following python modules are required.

* [py2app](https://pythonhosted.org/py2app/)
* [rumps](https://github.com/jaredks/rumps)

## License
```
The MIT License (MIT)

Copyright (c) 2016 Alfred Jiang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[![Analytics](https://ga-beacon.appspot.com/UA-76943272-1/autossp/readme?pixel)](https://github.com/igrigorik/ga-beacon)