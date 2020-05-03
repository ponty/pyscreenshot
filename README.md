The ``pyscreenshot`` module can be used to copy
the contents of the screen to a PIL_ or Pillow_ image memory using various back-ends.
Replacement for the [ImageGrab][15] Module, which works on Windows only,
so Windows users don't need this library.
For handling image memory (e.g. saving to file, converting,..) please read PIL_ or Pillow_ documentation.

Links:
 * home: https://github.com/ponty/pyscreenshot
 * PYPI: https://pypi.python.org/pypi/pyscreenshot

[![Build Status](https://travis-ci.org/ponty/pyscreenshot.svg?branch=master)](https://travis-ci.org/ponty/pyscreenshot)

Goal:
  Pyscreenshot tries to allow to take screenshots without installing 3rd party libraries.
  It is cross-platform but useful for Linux based distributions.
  It is only a pure Python wrapper, a thin layer over existing back-ends.
  Its strategy should work on most Linux distributions:
  a lot of back-ends are wrapped, if at least one exists then it works,
  if not then one back-end should be installed.

Features:
 * Cross-platform wrapper
 * Capturing the whole desktop
 * Capturing an area
 * saving to PIL_ or Pillow_ image memory
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
 * time taken: 0.1s - 2.0s
 * Performance is not a target for this library, but you can benchmark the back-ends and choose the fastest one.
 * Interactivity is not supported.
 * Mouse pointer is not visible.

Known problems:
 * gnome-screenshot_ back-end does not check $DISPLAY -> not working with Xvfb

Examples
========

grab and show the whole screen (examples/showgrabfullscreen.py):

```python
import pyscreenshot as ImageGrab

if __name__ == '__main__':

    # grab fullscreen
    im = ImageGrab.grab()

    # save image file
    im.save('screenshot.png')

    # show image in a window
    im.show()
```

to start the example:

```console
$ python3 -m pyscreenshot.examples.showgrabfullscreen
```

grab and show the part of the screen (examples/showgrabbox.py):

```python
import pyscreenshot as ImageGrab

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.show()
```

to start the example:

```console
$ python3 -m pyscreenshot.examples.showgrabbox
```

Installation
============

 * install Pillow_ (Ubuntu: ``sudo apt-get install python3-pil``)
 * install at least one back-end
 * install the program:

```console
$ python3 -m pip install pyscreenshot
```


Command line interface
======================

Back-end performance:

The performance can be checked with pyscreenshot.check.speedtest.

Example:

```console
python3 -m pyscreenshot.check.speedtest --virtual-display 2>/dev/null

n=10
------------------------------------------------------
scrot               	6.1  sec	(  608 ms per call)
imagemagick         	9.7  sec	(  969 ms per call)
wx                  	4.1  sec	(  408 ms per call)
pygdk3              	3.3  sec	(  328 ms per call)
qtpy                	6.9  sec	(  687 ms per call)
pyqt5               	6.9  sec	(  687 ms per call)
pyqt                	6.4  sec	(  644 ms per call)
pyside2             	6.7  sec	(  671 ms per call)
pyside              	6.5  sec	(  652 ms per call)
gnome-screenshot    	12   sec	( 1209 ms per call)
```

Print versions:

```console
python3 -m pyscreenshot.check.versions 2> /dev/null
python               3.7.3
pyscreenshot         0.7
scrot                1.1.1
imagemagick          6.9.10
wx                   4.0.4
pygdk3               3.32.0
qtpy                 1.3.1
pyqt5                5.12.1
pyqt                 4.12.1
pyside2              5.11.2
pyside               1.2.2
pygtk                missing
gnome-screenshot     3.30.0
```

Wayland
=======

On Wayland only the `gnome-screenshot` back-end works:

```python
im = ImageGrab.grab(backend='gnome-screenshot')
```

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
