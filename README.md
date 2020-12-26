The ``pyscreenshot`` module can be used to copy
the contents of the screen to a [PIL][5] or [Pillow][6]  image memory using various back-ends.
Replacement for the [ImageGrab][15] Module, which works on Windows and macOS only,
so Windows/macOS users don't need this library, except if they need better performance.
For handling image memory (e.g. saving to file, converting,..) please read [Pillow][6]  documentation.

Links:
 * home: https://github.com/ponty/pyscreenshot
 * PYPI: https://pypi.python.org/pypi/pyscreenshot

[![Build Status](https://travis-ci.org/ponty/pyscreenshot.svg?branch=master)](https://travis-ci.org/ponty/pyscreenshot)

Goal:
  Pyscreenshot tries to allow to take screenshots without installing 3rd party libraries.
  It is cross-platform but mainly useful for Linux based distributions.
  It is only a pure Python wrapper, a thin layer over existing back-ends.
  Its strategy should work on most Linux distributions:
  a lot of back-ends are wrapped, if at least one exists then it works,
  if not then one back-end should be installed.

Features:
 * Cross-platform wrapper
 * Capturing the whole desktop or an area
 * saving to [PIL][5] or [Pillow][6]  image memory
 * some back-ends are based on this discussion: http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux
 * pure Python library
 * supported Python versions: 2.7, 3.6, 3.7, 3.8
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
 * Performance is not a target for this library, but you can benchmark the possible settings and choose the fastest one.
 * Interactivity is not supported.
 * Mouse pointer is not visible.

Known problems:
 * KDE Wayland has on screen notification

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

The performance can be checked with pyscreenshot.check.speedtest module.
Backends are started in a subprocess with default (safest) settings 
which is necessary to isolate them from the main process and from each other. 
Disabling this option makes performance much better, but it may cause problems in some cases.

Test on Ubuntu 19.10 X11
<!-- embedme doc/gen/python3_-m_pyscreenshot.check.speedtest.txt -->
```console
$ python3 -m pyscreenshot.check.speedtest

n=10
------------------------------------------------------
default             	1    sec	(  102 ms per call)
pil                 	
mss                 	2.1  sec	(  214 ms per call)
scrot               	1    sec	(  101 ms per call)
maim                	1.5  sec	(  147 ms per call)
imagemagick         	2.5  sec	(  247 ms per call)
pyqt5               	4.4  sec	(  442 ms per call)
pyqt                	3.5  sec	(  352 ms per call)
pyside2             	5    sec	(  495 ms per call)
pyside              	3.5  sec	(  350 ms per call)
wx                  	3.3  sec	(  329 ms per call)
pygdk3              	2.3  sec	(  225 ms per call)
mac_screencapture   	
mac_quartz          	
gnome_dbus          	1.7  sec	(  166 ms per call)
gnome-screenshot    	2.3  sec	(  231 ms per call)
kwin_dbus           	
```
<!-- embedme doc/gen/python3_-m_pyscreenshot.check.speedtest_--childprocess_0.txt -->
```console
$ python3 -m pyscreenshot.check.speedtest --childprocess 0

n=10
------------------------------------------------------
default             	0.16 sec	(   16 ms per call)
pil                 	
mss                 	0.17 sec	(   17 ms per call)
scrot               	1    sec	(  104 ms per call)
maim                	1.5  sec	(  145 ms per call)
imagemagick         	2.5  sec	(  246 ms per call)
pyqt5               	1.1  sec	(  110 ms per call)
pyqt                	1    sec	(  104 ms per call)
pyside2             	1.2  sec	(  121 ms per call)
pyside              	1    sec	(  104 ms per call)
wx                  	0.33 sec	(   32 ms per call)
pygdk3              	0.2  sec	(   19 ms per call)
mac_screencapture   	
mac_quartz          	
gnome_dbus          	1.5  sec	(  152 ms per call)
gnome-screenshot    	2.3  sec	(  230 ms per call)
kwin_dbus           	
```


You can force a backend:
```python
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="scrot")
```

You can force if subprocess is applied, setting it to False together with mss gives the best performance:
```python
# best performance
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="mss", childprocess=False)
```



Printing beckend versions:
<!-- embedme doc/gen/python3_-m_pyscreenshot.check.versions.txt -->

```console
$ python3 -m pyscreenshot.check.versions
python               3.7.5
pyscreenshot         2.2
pil                  7.0.0
mss                  5.1.0
scrot                1.1.1
maim                 5.5
imagemagick          6.9.10
pyqt5                5.12.3
pyqt                 4.12.1
pyside2              5.14.2.1
pyside               1.2.2
wx                   4.0.6
pygdk3               3.34.0
mac_screencapture    
mac_quartz           
gnome_dbus           ?.?
gnome-screenshot     3.33.90
kwin_dbus            ?.?
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
[5]: http://www.pythonware.com/library/pil/
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
