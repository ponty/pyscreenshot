The ``pyscreenshot`` module can be used to copy
the contents of the screen to a PIL_ or Pillow_ image memory.
Replacement for the ImageGrab_ Module, which works on Windows only.
For handling image memory (e.g. saving to file, converting,..) please read PIL_ or Pillow_ documentation.

Links:
 * home: https://github.com/ponty/pyscreenshot
 * documentation: http://ponty.github.com/pyscreenshot

Goal:
  Pyscreenshot tries to allow to take screenshots without installing 3rd party libraries.
  It is cross-platform but useful for Linux based distributions.
  It is only a pure Python wrapper, a thin layer over existing back-ends.
  Its strategy should work on most Linux distributions:
  a lot of back-ends are wrapped, if at least one exists then it works,
  if not then one back-end should be installed.
  Performance and interactivity are not important for this library.

Features:
 * Cross-platform wrapper
 * Capturing the whole desktop
 * Capturing an area
 * saving to PIL_ or Pillow_ image memory
 * some back-ends are based on this discussion: http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux
 * pure Python library
 * supported python versions: 2.6, 2.7
 * Plugin based, it has wrappers for various back-ends:
     * scrot_
     * ImageMagick_
     * PyGTK_
     * PIL_ or Pillow_ (only on windows)
     * PyQt4_
     * wxPython_

Known problems:
 * different back-ends generate slightly different images from the same desktop,
   this should be investigated
 * ImageMagick_ creates blackbox_ on some systems
 * PyGTK_ back-end does not check $DISPLAY -> not working with Xvfb
 * slow: 0.2s - 0.7s

Similar projects:
 - http://sourceforge.net/projects/gtkshots/
 - http://pypi.python.org/pypi/autopy


Usage
============

Example::

    import pyscreenshot as ImageGrab

    # fullscreen
    im=ImageGrab.grab()
    im.show()

    # part of the screen
    im=ImageGrab.grab(bbox=(10,10,510,510)) # X1,Y1,X2,Y2
    im.show()

Installation
============

General
--------

 * install pip_
 * install PIL_ or Pillow_
 * install at least one back-end
 * install the program::

    # as root
    pip install pyscreenshot

Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo pip install pyscreenshot
    sudo apt-get install python-imaging
    # optional back-ends
    sudo apt-get install scrot
    sudo apt-get install imagemagick
    sudo apt-get install python-gtk2
    sudo apt-get install python-qt4
    # optional for examples
    sudo pip install entrypoint2

Uninstall
----------
::

    # as root
    pip uninstall pyscreenshot



.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _ImageGrab: http://pillow.readthedocs.org/en/latest/reference/ImageGrab.html
.. _PIL: http://www.pythonware.com/library/pil/
.. _Pillow: http://pillow.readthedocs.org
.. _ImageMagick: http://www.imagemagick.org/
.. _PyGTK: http://www.pygtk.org/
.. _blackbox: http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=13658
.. _scrot: http://en.wikipedia.org/wiki/Scrot
.. _PyQt4: http://www.riverbankcomputing.co.uk/software/pyqt
.. _wxPython: http://www.wxpython.org/
