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
 * supported Python versions: 2.7, 3.5, 3.6, 3.7, 3.8
 * It has wrappers for various back-ends:
     * scrot_
     * ImageMagick_
     * PyGTK_
     * PIL_ or Pillow_ (only on Windows)
     * PyQt4_
     * PyQt5_
     * PySide_
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

    python -m pyscreenshot.examples.showgrabfullscreen

grab and show the part of the screen::

  #-- include('examples/showgrabbox.py')--#
  import pyscreenshot as ImageGrab

  if __name__ == '__main__':
      # part of the screen
      im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
      im.show()
  #-#

to start the example::

    python -m pyscreenshot.examples.showgrabbox

Installation
============

 * install pip_
 * install Pillow_ (Ubuntu: ``sudo apt-get install python-pil``)
 * install at least one back-end
 * install the program::

    pip install pyscreenshot


Uninstall::

    pip uninstall pyscreenshot


Command line interface
======================

Back-end performance::

  The performance can be checked with pyscreenshot.check.speedtest.

  Example:

  #-- sh('python -m pyscreenshot.check.speedtest --virtual-display 2>/dev/null') --#

  n=10
  ------------------------------------------------------
  wx                  	3.4  sec	(  343 ms per call)
  pygtk               	5.6  sec	(  558 ms per call)
  pygdk3              	2.8  sec	(  275 ms per call)
  pyqt                	5.7  sec	(  565 ms per call)
  pyqt5               	5.3  sec	(  527 ms per call)
  scrot               	4.8  sec	(  481 ms per call)
  imagemagick         	7.5  sec	(  750 ms per call)
  pyside              	5.6  sec	(  558 ms per call)
  gnome-screenshot    	13   sec	( 1278 ms per call)
  #-#


Print versions::

  #-- sh('python -m pyscreenshot.check.versions 2> /dev/null ')--#
  python               2.7.15rc1
  pyscreenshot         0.4.2
  wx                   3.0.2.0
  pygtk                2.28.6
  pygdk3               3.26.1
  pyqt                 4.12.1
  pyqt5                5.10.1
  scrot                0.8
  imagemagick          6.9.7
  pyside               1.2.2
  gnome-screenshot     3.25.0
  #-#


Wayland
=======

On Wayland only the `gnome-screenshot` back-end works::

 im = ImageGrab.grab(backend='gnome-screenshot')



.. _pip: https://pypi.python.org/pypi/pip
.. _ImageGrab: http://pillow.readthedocs.org/en/latest/reference/ImageGrab.html
.. _PIL: http://www.pythonware.com/library/pil/
.. _Pillow: http://pillow.readthedocs.org
.. _ImageMagick: http://www.imagemagick.org/
.. _PyGTK: http://www.pygtk.org/
.. _blackbox: http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=13658
.. _scrot: http://en.wikipedia.org/wiki/Scrot
.. _PyQt4: http://pyqt.sourceforge.net/Docs/PyQt4/index.html
.. _PyQt5: http://pyqt.sourceforge.net/Docs/PyQt5/index.html
.. _PySide: http://www.pyside.org/
.. _wxPython: http://www.wxpython.org/
.. _gnome-screenshot: https://git.gnome.org/browse/gnome-screenshot/

.. |Travis| image:: http://img.shields.io/travis/ponty/pyscreenshot.svg
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
