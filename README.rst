The ``pyscreenshot`` module can be used to copy
the contents of the screen to a PIL_ or Pillow_ image memory using various back-ends.
Replacement for the ImageGrab_ Module, which works on Windows only,
so Windows users don't need this library.
For handling image memory (e.g. saving to file, converting,..) please read PIL_ or Pillow_ documentation.

Links:
 * home: https://github.com/ponty/pyscreenshot
 * documentation: http://pyscreenshot.readthedocs.org
 * PYPI: https://pypi.python.org/pypi/pyscreenshot

|Travis| |Coveralls| |Latest Version| |Supported Python versions| |License| |Documentation|

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
     * scrot_
     * ImageMagick_
     * PyGTK_
     * PIL_ or Pillow_ (only on Windows)
     * PyQt4_
     * PyQt5_
     * PySide_
     * PySide2_
     * QtPy_
     * wxPython_
     * Quartz (Mac)
     * screencapture (Mac)
     * gnome-screenshot_
 * time taken: 0.1s - 2.0s
 * Performance is not a target for this library, but you can benchmark the back-ends and choose the fastest one.
 * Interactivity is not supported.
 * Mouse pointer is not visible.

Known problems:
 * ImageMagick_ creates blackbox_ on some systems
 * gnome-screenshot_ back-end does not check $DISPLAY -> not working with Xvfb

Similar projects:
 - http://sourceforge.net/projects/gtkshots/
 - http://pypi.python.org/pypi/autopy
 - https://github.com/asweigart/pyscreeze


Examples
========

grab and show the whole screen::

  #-- include('examples/showgrabfullscreen.py') --#
  import pyscreenshot as ImageGrab

  if __name__ == '__main__':

      # grab fullscreen
      im = ImageGrab.grab()

      # save image file
      im.save('screenshot.png')

      # show image in a window
      im.show()
  #-#

to start the example::

    python3 -m pyscreenshot.examples.showgrabfullscreen

grab and show the part of the screen::

  #-- include('examples/showgrabbox.py')--#
  import pyscreenshot as ImageGrab

  if __name__ == '__main__':
      # part of the screen
      im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
      im.show()
  #-#

to start the example::

    python3 -m pyscreenshot.examples.showgrabbox

Installation
============

 * install Pillow_ (Ubuntu: ``sudo apt-get install python3-pil``)
 * install at least one back-end
 * install the program::

    pip3 install pyscreenshot



Command line interface
======================

Back-end performance::

  The performance can be checked with pyscreenshot.check.speedtest.

  Example:

  #-- sh('python3 -m pyscreenshot.check.speedtest --virtual-display 2>/dev/null') --#

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
  #-#


Print versions::

  #-- sh('python3 -m pyscreenshot.check.versions 2> /dev/null ')--#
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
  #-#


Wayland
=======

On Wayland only the `gnome-screenshot` back-end works::

 im = ImageGrab.grab(backend='gnome-screenshot')



.. _ImageGrab: http://pillow.readthedocs.org/en/latest/reference/ImageGrab.html
.. _PIL: http://www.pythonware.com/library/pil/
.. _Pillow: https://pypi.org/project/Pillow/
.. _ImageMagick: http://www.imagemagick.org/
.. _PyGTK: https://pypi.org/project/PyGTK/
.. _blackbox: http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=13658
.. _scrot: http://en.wikipedia.org/wiki/Scrot
.. _PyQt4: https://pypi.org/project/PyQt4/
.. _PyQt5: https://pypi.org/project/PyQt5/
.. _PySide: https://pypi.org/project/PySide/
.. _PySide2: https://pypi.org/project/PySide2/
.. _QtPy: https://github.com/spyder-ide/qtpy
.. _wxPython: http://www.wxpython.org/
.. _gnome-screenshot: https://git.gnome.org/browse/gnome-screenshot/

.. |Travis| image:: https://travis-ci.org/ponty/pyscreenshot.svg?branch=master
   :target: https://travis-ci.org/ponty/pyscreenshot/
.. |Coveralls| image:: http://img.shields.io/coveralls/ponty/pyscreenshot/master.svg
   :target: https://coveralls.io/r/ponty/pyscreenshot/
.. |Latest Version| image:: https://img.shields.io/pypi/v/pyscreenshot.svg
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/pyscreenshot.svg
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |License| image:: https://img.shields.io/pypi/l/pyscreenshot.svg
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |Documentation| image:: https://readthedocs.org/projects/pyscreenshot/badge/?version=latest
   :target: http://pyscreenshot.readthedocs.org
