TL;DR: Use [Pillow][15]. If Pillow doesn't work or it's slow then try pyscreenshot.

The ``pyscreenshot`` module is obsolete in most cases.
It was created because [PIL][5] ImageGrab module worked on Windows only,
but now Linux and macOS are also [supported][15] by Pillow.
There are some features in ``pyscreenshot`` which can be useful in special cases:
flexible backends with the same interface, Wayland support, sometimes better performance, optional subprocessing.

The module can be used to copy the contents of the screen to a [Pillow][6] image memory
using various back-ends. Replacement for the [ImageGrab][15] Module.

For handling image memory (e.g. saving to file, converting,..) please read [Pillow][6]  documentation.

Links:

* home: https://github.com/ponty/pyscreenshot
* PYPI: https://pypi.python.org/pypi/pyscreenshot

![workflow](https://github.com/ponty/pyscreenshot/actions/workflows/main.yml/badge.svg)

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
* supported Python versions: 3.9, 3.10, 3.11
* It has wrappers for various back-ends:
  * [Pillow][6] (X11, Linux gnome-screenshot, Win, macOS screencapture)
  * [Python MSS][14] (X11, Win, macOS)
  * [xdg-desktop-portal][20] (D-Bus: org.freedesktop.portal.Screenshot) (X11, Wayland)
  * GNOME (D-Bus: org.gnome.Shell.Screenshot) (Gnome X11/Wayland)
  * [scrot][1] (X11)
  * [maim][2] (X11)
  * [ImageMagick][3] (X11)
  * [PyQt5][8] (X11, Win, macOS)
  * [PySide2][10] (X11, Win, macOS)
  * [wxPython][12] (X11, Win, macOS)
  * [gnome-screenshot][13] (X11, Gnome Wayland)
  * [Grim][19] (Sway Wayland)
  * Quartz (macOS)
  * screencapture (macOS)
* Old removed backends: 
  * PyGTK
  * QtPy, 
  * [PySide][9]
  * [PyQt4][7]
  * KDE Plasma (D-Bus: org.kde.kwin.Screenshot)
* Performance is not the main target for this library, but you can benchmark the possible settings and choose the fastest one.
* Interactivity is not supported.
* Mouse pointer is not visible.

Known problems:

* KDE Wayland has on screen notification
* gnome-screenshot has Flash effect (https://bugzilla.gnome.org/show_bug.cgi?id=672759)
* xdg-desktop-portal can have confirmation dialog box
  
Comparison:

| system                        | pyscreenshot 3.1 | pillow 9.4.0 | mss 7.0.1 |
| ----------------------------- | :--------------: | :----------: | :-------: |
| Ubuntu 22.04                  |        ✅         |      ❌       |     ❌     |
| Kubuntu 22.04                 |        ✅         |      ✅       |     ✅     |
| Xubuntu 22.04                 |        ✅         |      ✅       |     ✅     |
| Lubuntu 22.04                 |        ✅         |      ✅       |     ✅     |
| Ubuntu Server 22.04+sway+grim |        ✅         |      ❌       |     ❌     |


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
        sleep(1)  # wait for displaying window
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

Test on Ubuntu 22.04 X11

Versions:

<!-- embedme doc/gen/python3_-m_pyscreenshot.check.versions.txt -->

```console
$ python3 -m pyscreenshot.check.versions
python               3.10.6
pyscreenshot         3.1
pil                  9.0.1
mss                  7.0.1
scrot                1.7
grim                 ?.?
maim                 5.6.3
imagemagick          6.9.11
pyqt5                5.15.6
pyside2              5.15.2
wx                   4.0.7
pygdk3               3.42.1
mac_screencapture    
mac_quartz           
freedesktop_dbus     ?.?
gnome_dbus           ?.?
gnome-screenshot     41.0
```

Backends are started in a subprocess (safest):

<!-- embedme doc/gen/python3_-m_pyscreenshot.check.speedtest.txt -->

```console
$ python3 -m pyscreenshot.check.speedtest

n=10
------------------------------------------------------
default             	1    sec	(  100 ms per call)
pil                 	1.7  sec	(  167 ms per call)
mss                 	2    sec	(  197 ms per call)
scrot               	1    sec	(  100 ms per call)
grim                	
maim                	1.4  sec	(  135 ms per call)
imagemagick         	2.2  sec	(  221 ms per call)
pyqt5               	4    sec	(  403 ms per call)
pyside2             	3.9  sec	(  394 ms per call)
wx                  	2.9  sec	(  293 ms per call)
pygdk3              	2.2  sec	(  218 ms per call)
mac_screencapture   	
mac_quartz          	
gnome_dbus          	
gnome-screenshot    	4    sec	(  401 ms per call)
```

Backends are started without subprocess (fastest):

<!-- embedme doc/gen/python3_-m_pyscreenshot.check.speedtest_--childprocess_0.txt -->

```console
$ python3 -m pyscreenshot.check.speedtest --childprocess 0

n=10
------------------------------------------------------
default             	0.13 sec	(   12 ms per call)
pil                 	0.12 sec	(   11 ms per call)
mss                 	0.2  sec	(   19 ms per call)
scrot               	1    sec	(   99 ms per call)
grim                	
maim                	1.3  sec	(  134 ms per call)
imagemagick         	2.2  sec	(  218 ms per call)
pyqt5               	1    sec	(  104 ms per call)
pyside2             	1    sec	(  101 ms per call)
wx                  	0.34 sec	(   33 ms per call)
pygdk3              	0.23 sec	(   23 ms per call)
mac_screencapture   	
mac_quartz          	
gnome_dbus          	
gnome-screenshot    	4.4  sec	(  437 ms per call)
```

You can force a backend:

```python
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="scrot")
```

You can force if subprocess is applied, setting it to False together with `mss` or `pil` gives the best performance in most cases:

```python
# best performance
import pyscreenshot as ImageGrab
im = ImageGrab.grab(backend="mss", childprocess=False)
```

Wayland
=======

Wayland is supported with these setups:

1. using D-Bus (org.freedesktop.portal.Screenshot) on any desktop with xdg-desktop-portal.
2. using D-Bus (org.gnome.Shell.Screenshot) on GNOME.
3. using [Grim][19] on any Wayland compositor with wlr-screencopy-unstable-v1 support. (GNOME:no, KDE:no, Sway:yes)

If both Wayland and X are available then Wayland is preferred
because Xwayland can not be used for screenshot. Rules for decision:

1. use X if DISPLAY variable exists and XDG_SESSION_TYPE variable != "wayland"
2. use Wayland if 1. is not successful

Dependencies
============

Only pure python modules are used:

1. [EasyProcess][17] for calling programs
2. [entrypoint2][18] for generating command line interface
3. [MSS][14] backend is added because it is very fast and pure and multiplatform
4. [jeepney][16] for D-Bus calls

Test
====

Some Linux distributions can be tested with VirtualBox and Vagrant:

```console
$ ./tests/vagrant/vagrant_boxes.py
```

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
[20]: https://github.com/flatpak/xdg-desktop-portal
