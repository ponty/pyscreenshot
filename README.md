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
     * [PyGTK][4]
     * [PIL][5] or [Pillow][6] (only on Windows)
     * [PyQt4][7]
     * [PyQt5][8]
     * [PySide][9]
     * [PySide2][10]
     * [QtPy][11]
     * [wxPython][12]
     * Quartz (Mac)
     * screencapture (Mac)
     * [gnome-screenshot][13]
     * Python [MSS][14]
 * Performance is not a target for this library, but you can benchmark the back-ends and choose the fastest one.
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

grab and show the whole screen (examples/showgrabfullscreen.py):

```python
import pyscreenshot as ImageGrab

# grab fullscreen
im = ImageGrab.grab()

# save image file
im.save('fullscreen.png')
```

grab and show the part of the screen (examples/showgrabbox.py):

```python
import pyscreenshot as ImageGrab

# part of the screen
im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2

# save image file
im.save('box.png')
```


Performance
===========

The performance can be checked with pyscreenshot.check.speedtest module.
Some backends are started in subprocess with default (safest) settings 
which is necessary to isolate them from the main process. 
This makes them slower as a disavantage.

Test on Ubuntu 19.10 X11
```console
$  python3 -m pyscreenshot.check.speedtest

n=10
------------------------------------------------------
default             	0.16 sec	(   15 ms per call)
pil                 	
mss                 	0.16 sec	(   15 ms per call)
scrot               	1    sec	(  103 ms per call)
maim                	1.5  sec	(  145 ms per call)
imagemagick         	2.1  sec	(  214 ms per call)
qtpy                	4.5  sec	(  452 ms per call) [subprocess]
pyqt5               	4.3  sec	(  433 ms per call) [subprocess]
pyqt                	3.8  sec	(  379 ms per call) [subprocess]
pyside2             	5.1  sec	(  505 ms per call) [subprocess]
pyside              	3.6  sec	(  360 ms per call) [subprocess]
wx                  	3.2  sec	(  315 ms per call) [subprocess]
pygdk3              	0.2  sec	(   19 ms per call)
pygtk               	
mac_screencapture   	
mac_quartz          	
gnome_dbus          	1.4  sec	(  144 ms per call)
gnome-screenshot    	3.7  sec	(  369 ms per call)
kwin_dbus           	  	
```

You can force a backend:
```python
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="scrot")
```

You can even force if subprocess is applied:
```python
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="pyqt5", childprocess=False)
```

Printing beckend versions:

```console
$ python3 -m pyscreenshot.check.versions 
python               3.7.5
pyscreenshot         2.0
pil                  7.0.0
mss                  5.1.0
scrot                1.1.1
maim                 5.5
imagemagick          6.9.10
qtpy                 1.3.1
pyqt5                5.12.3
pyqt                 4.12.1
pyside2              5.14.2.1
pyside               1.2.2
wx                   4.0.6
pygdk3               3.34.0
pygtk                
mac_screencapture    
mac_quartz           
gnome_dbus           ?.?
gnome-screenshot     3.33.90
kwin_dbus            ?.?
```

Wayland
=======

Wayland is supported only on Python3 using D-Bus on Gnome and KDE.
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
3. [MSS][14] backend is added because it is very fast and pure and multiplatform, 
    so it will be the first choice in most cases (Python3 only)
4. [jeepney][16] for D-Bus calls (Python3 only)

Hierarchy
=========

![Alt text](https://g.gravizo.com/source/svg?https%3A%2F%2Fraw.githubusercontent.com/ponty/pyscreenshot/master/hierarchy.dot)

[1]: http://en.wikipedia.org/wiki/Scrot
[2]: https://github.com/naelstrof/maim
[3]: http://www.imagemagick.org/
[4]: https://pypi.org/project/PyGTK/
[5]: http://www.pythonware.com/library/pil/
[6]: https://pypi.org/project/Pillow/
[7]: https://pypi.org/project/PyQt4/
[8]: https://pypi.org/project/PyQt5/
[9]: https://pypi.org/project/PySide/
[10]: https://pypi.org/project/PySide2/
[11]: https://github.com/spyder-ide/qtpy
[12]: http://www.wxpython.org/
[13]: https://git.gnome.org/browse/gnome-screenshot/
[14]: https://github.com/BoboTiG/python-mss
[15]: http://pillow.readthedocs.org/en/latest/reference/ImageGrab.html
[16]: https://pypi.org/project/jeepney/
[17]: https://github.com/ponty/EasyProcess
[18]: https://github.com/ponty/entrypoint2