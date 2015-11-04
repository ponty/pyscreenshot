The ``pyscreenshot`` module can be used to copy
the contents of the screen to a PIL_ or Pillow_ image memory.
Replacement for the ImageGrab_ Module, which works on Windows only.
For handling image memory (e.g. saving to file, converting,..) please read PIL_ or Pillow_ documentation.

Links:
 * home: https://github.com/ponty/pyscreenshot
 * documentation: http://pyscreenshot.readthedocs.org
 * PYPI: https://pypi.python.org/pypi/pyscreenshot

|Travis| |Coveralls| |Latest Version| |Supported Python versions| |License| |Downloads| |Code Health| |Documentation|

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
 * supported python versions: 2.6, 2.7, 3.3, 3.4, 3.5
 * Plugin based, it has wrappers for various back-ends:
     * scrot_
     * ImageMagick_
     * PyGTK_
     * PIL_ or Pillow_ (only on windows)
     * PyQt4_
     * wxPython_
     * Quartz (Mac)
     * screencapture (Mac)
 * time: 0.1s - 1.0s

Known problems:
 * ImageMagick_ creates blackbox_ on some systems
 * PyGTK_ back-end does not check $DISPLAY -> not working with Xvfb

Similar projects:
 - http://sourceforge.net/projects/gtkshots/
 - http://pypi.python.org/pypi/autopy


Examples
========

grab and show the whole screen::
  
  #-- include('examples/showgrabfullscreen.py') --#
  import pyscreenshot as ImageGrab

  if __name__ == "__main__":
      # fullscreen
      im=ImageGrab.grab()
      im.show()
  #-#

to start the example:: 

    python -m pyscreenshot.examples.showgrabfullscreen

grab and show the part of the screen ::

  #-- include('examples/showgrabbox.py')--#
  import pyscreenshot as ImageGrab

  if __name__ == "__main__":
      # part of the screen
      im=ImageGrab.grab(bbox=(10,10,510,510)) # X1,Y1,X2,Y2
      im.show()
  #-#

to start the example:: 

    python -m pyscreenshot.examples.showgrabbox

Installation
============

General
-------

 * install pip_
 * install PIL_ or Pillow_
 * install at least one back-end
 * install the program::

    # as root
    pip install pyscreenshot

Ubuntu 14.04
------------
::

    sudo apt-get install python-pip
    sudo apt-get install python-pil
    sudo pip install pyscreenshot
    # optional back-ends
    sudo apt-get install scrot imagemagick python-gtk2 python-qt4 python-wxgtk2.8
    # optional for examples
    sudo pip install entrypoint2

Uninstall
---------
::

    # as root
    pip uninstall pyscreenshot


Command line interface
======================

Back-end performance::

  The performance can be checked with pyscreenshot.check.speedtest.
  
  Example:
  
  #-- sh('python -m pyscreenshot.check.speedtest --virtual-display 2>/dev/null') --#

  n=10	 to_file: True	 bounding box: None
  ------------------------------------------------------
  wx                  	1.3  sec	(  130 ms per call)
  pygtk               	1    sec	(  100 ms per call)
  pyqt                	1.1  sec	(  109 ms per call)
  scrot               	0.71 sec	(   70 ms per call)
  imagemagick         	0.64 sec	(   64 ms per call)

  n=10	 to_file: False	 bounding box: None
  ------------------------------------------------------
  wx                  	1.1  sec	(  109 ms per call)
  pygtk               	1.3  sec	(  126 ms per call)
  pyqt                	1.4  sec	(  135 ms per call)
  scrot               	0.94 sec	(   94 ms per call)
  imagemagick         	0.78 sec	(   78 ms per call)

  n=10	 to_file: False	 bounding box: (10, 10, 20, 20)
  ------------------------------------------------------
  wx                  	1    sec	(  101 ms per call)
  pygtk               	0.62 sec	(   61 ms per call)
  pyqt                	1.3  sec	(  127 ms per call)
  scrot               	0.87 sec	(   87 ms per call)
  imagemagick         	0.58 sec	(   57 ms per call)
  #-#


Print versions::

  #-- sh('python -m pyscreenshot.check.versions 2> /dev/null ')--#
  pyscreenshot         0.3.4
  wx                   2.8.12.1
  pygtk                2.28.6
  pyqt                 not implemented
  scrot                0.8
  imagemagick          6.7.7
  #-#


command line help
=================

::

  #-- sh('python -m pyscreenshot.check.speedtest --help')--#
  usage: speedtest.py [-h] [-v] [--debug]

  optional arguments:
    -h, --help            show this help message and exit
    -v, --virtual-display
    --debug               set logging level to DEBUG
  #-#

::

  #-- sh('python -m pyscreenshot.check.versions --help')--#
  usage: versions.py [-h] [--debug]

  optional arguments:
    -h, --help  show this help message and exit
    --debug     set logging level to DEBUG
  #-#



.. _pip: https://pypi.python.org/pypi/pip
.. _ImageGrab: http://pillow.readthedocs.org/en/latest/reference/ImageGrab.html
.. _PIL: http://www.pythonware.com/library/pil/
.. _Pillow: http://pillow.readthedocs.org
.. _ImageMagick: http://www.imagemagick.org/
.. _PyGTK: http://www.pygtk.org/
.. _blackbox: http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=13658
.. _scrot: http://en.wikipedia.org/wiki/Scrot
.. _PyQt4: http://www.riverbankcomputing.co.uk/software/pyqt
.. _wxPython: http://www.wxpython.org/

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
.. |Downloads| image:: https://img.shields.io/pypi/dm/pyscreenshot.svg
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |Code Health| image:: https://landscape.io/github/ponty/pyscreenshot/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ponty/pyscreenshot/master
.. |Documentation| image:: https://readthedocs.org/projects/pyscreenshot/badge/?version=latest
   :target: http://pyscreenshot.readthedocs.org
