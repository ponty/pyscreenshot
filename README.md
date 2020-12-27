The ``pyscreenshot`` module is obsolete in most cases.
It was created because [PIL][5] ImageGrab module worked on Windows only,
but now Linux and macOS are also [supported][15].
There are some features in ``pyscreenshot`` which can be useful in special cases:
flexible backends, Wayland support, sometimes better performance, optional subprocessing.

The module can be used to copy the contents of the screen to a [Pillow][6] image memory 
using various back-ends. Replacement for the [ImageGrab][15] Module.

For handling image memory (e.g. saving to file, converting,..) please read [Pillow][6]  documentation.

Links:
 * home: https://github.com/ponty/pyscreenshot
 * PYPI: https://pypi.python.org/pypi/pyscreenshot

[![Build Status](https://travis-ci.org/ponty/pyscreenshot.svg?branch=master)](https://travis-ci.org/ponty/pyscreenshot)

Goal:
  Pyscreenshot tries to allow to take screenshots without installing 3rd party libraries.
  It is cross-platform.
  It is only a pure Python wrapper, a thin layer over existing back-ends.
  Its strategy should work on most Linux distributions:
  a lot of back-ends are wrapped, if at least one exists then it works,
  if not then one back-end should be installed.

Features:
 * Cross-platform wrapper
 * Capturing the whole desktop or an area
 * saving to [Pillow][6] image memory
 * some back-ends are based on this discussion: http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux
 * pure Python library
 * supported Python versions: 2.7, 3.6, 3.7, 3.8, 3.9
 * It has wrappers for various back-ends:
     * [scrot][1]
     * [maim][2]
     * [ImageMagick][3]
     * [PIL][5] or [Pillow][6] (only on Windows)
     * [PyQt4][7]
     * [PyQt5][8]
     * [PySide][9]
     * [PySide2][10]
     * [wxPython][12]
     * Quartz (Mac)
     * screencapture (Mac)
     * [gnome-screenshot][13]
     * [Python MSS][14]
     * [Grim][19] (Only on Linux. For Wayland environments other than KDE and Gnome, like Sway)
 * Performance is not the main target for this library, but you can benchmark the possible settings and choose the fastest one.
 * Interactivity is not supported.
 * Mouse pointer is not visible.

Known problems:
 * KDE Wayland has on screen notification
 * gnome-screenshot has Flash effect (https://bugzilla.gnome.org/show_bug.cgi?id=672759)

Installation:

```console  
$ python3 -m pip install Pillow pyscreenshot
```


Examples
========

```py
# pyscreenshot/examples/grabfullscreen.py

"Grab the whole screen"
import pyscreenshot as ImageGrab

# grab fullscreen
im = ImageGrab.grab()

# save image file
im.save("fullscreen.png")

```

```py
# pyscreenshot/examples/grabbox.py

"Grab the part of the screen"
import pyscreenshot as ImageGrab

# part of the screen
im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2

# save image file
im.save("box.png")

```


```py
# pyscreenshot/examples/virtdisp.py

"Create screenshot of xmessage with Xvfb"
from time import sleep

from easyprocess import EasyProcess
from pyvirtualdisplay import Display

import pyscreenshot as ImageGrab

with Display(size=(100, 60)) as disp:  # start Xvfb display
    # display is available
    with EasyProcess(["xmessage", "hello"]):  # start xmessage
        sleep(1)  # wait for diplaying window
        img = ImageGrab.grab()
img.save("xmessage.png")

```

Image:

![](/doc/gen/xmessage.png)




Performance
===========

The performance can be checked with `pyscreenshot.check.speedtest` module.
Backends are started in a subprocess with default (safest) settings 
which is necessary to isolate them from the main process and from each other. 
Disabling this option makes performance much better, but it may cause problems in some cases.

Test on Ubuntu 20.04 X11

Versions:
<!-- embedme doc/gen/python3_-m_pyscreenshot.check.versions.txt -->

```console
$ python3 -m pyscreenshot.check.versions
python               3.8.5
pyscreenshot         2.3
pil                  8.0.1
mss                  6.1.0
scrot                1.2
grim                 ?.?
maim                 5.5.3
imagemagick          6.9.10
pyqt5                5.14.1
pyqt                 
pyside2              5.14.0
pyside               
wx                   4.0.7
pygdk3               3.36.0
mac_screencapture    
mac_quartz           
gnome_dbus           ?.?
gnome-screenshot     3.36.0
kwin_dbus            ?.?
```

<!-- embedme doc/gen/python3_-m_pyscreenshot.check.speedtest.txt -->
```console
$ python3 -m pyscreenshot.check.speedtest

n=10
------------------------------------------------------
default             	0.98 sec	(   98 ms per call)
pil                 	1.7  sec	(  169 ms per call)
mss                 	2    sec	(  196 ms per call)
scrot               	1    sec	(  102 ms per call)
grim                	
maim                	1.6  sec	(  156 ms per call)
imagemagick         	2.5  sec	(  246 ms per call)
pyqt5               	4.3  sec	(  432 ms per call)
pyqt                	
pyside2             	4.2  sec	(  423 ms per call)
pyside              	
wx                  	4.4  sec	(  435 ms per call)
pygdk3              	2.1  sec	(  205 ms per call)
mac_screencapture   	
mac_quartz          	
gnome_dbus          	1.5  sec	(  147 ms per call)
gnome-screenshot    	4    sec	(  397 ms per call)
kwin_dbus           	
```
<!-- embedme doc/gen/python3_-m_pyscreenshot.check.speedtest_--childprocess_0.txt -->
```console
$ python3 -m pyscreenshot.check.speedtest --childprocess 0

n=10
------------------------------------------------------
default             	0.15 sec	(   15 ms per call)
pil                 	0.09 sec	(    8 ms per call)
mss                 	0.17 sec	(   17 ms per call)
scrot               	0.96 sec	(   95 ms per call)
grim                	
maim                	1.4  sec	(  143 ms per call)
imagemagick         	2.3  sec	(  233 ms per call)
pyqt5               	1.1  sec	(  113 ms per call)
pyqt                	
pyside2             	1.1  sec	(  108 ms per call)
pyside              	
wx                  	0.47 sec	(   46 ms per call)
pygdk3              	0.18 sec	(   17 ms per call)
mac_screencapture   	
mac_quartz          	
gnome_dbus          	1.5  sec	(  149 ms per call)
gnome-screenshot    	3.8  sec	(  384 ms per call)
kwin_dbus           	
```


You can force a backend:
```python
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="scrot")
```

You can force if subprocess is applied, setting it to False together with `mss` gives the best performance in most cases:
```python
# best performance
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="mss", childprocess=False)
```

Wayland
=======

Wayland is supported with two setups:
1. using D-Bus on Gnome or KDE. Python 3 only.
2. using [Grim][19] on any Wayland compositor with wlr-screencopy-unstable-v1 support. (Gnome:no, KDE:no, Sway:yes)

If both Wayland and X are available then Wayland is preferred
because Xwayland can not be used for screenshot.  
Rules for decision:
 1. use X if DISPLAY variable exists and XDG_SESSION_TYPE variable != "wayland"
 2. use Wayland if 1. is not successful

Dependencies
============

Only pure python modules are used:
1. [EasyProcess][17] for calling programs
2. [entrypoint2][18] for generating command line interface
3. [MSS][14] backend is added because it is very fast and pure and multiplatform (Python3 only)
4. [jeepney][16] for D-Bus calls (Python3 only)

Hierarchy
=========

![Alt text](https://g.gravizo.com/source/svg?https%3A%2F%2Fraw.githubusercontent.com/ponty/pyscreenshot/master/doc/hierarchy.dot)

[1]: https://en.wikipedia.org/wiki/Scrot
[2]: https://github.com/naelstrof/maim
[3]: https://www.imagemagick.org/
[5]: https://en.wikipedia.org/wiki/Python_Imaging_Library
[6]: https://pypi.org/project/Pillow/
[7]: https://pypi.org/project/PyQt4/
[8]: https://pypi.org/project/PyQt5/
[9]: https://pypi.org/project/PySide/
[10]: https://pypi.org/project/PySide2/
[12]: https://www.wxpython.org/
[13]: https://git.gnome.org/browse/gnome-screenshot/
[14]: https://github.com/BoboTiG/python-mss
[15]: https://pillow.readthedocs.org/en/latest/reference/ImageGrab.html
[16]: https://pypi.org/project/jeepney/
[17]: https://github.com/ponty/EasyProcess
[18]: https://github.com/ponty/entrypoint2
[19]: https://github.com/emersion/grim
