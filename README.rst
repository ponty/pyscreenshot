The ``pyscreenshot`` module can be used to copy
the contents of the screen to a PIL_ or Pillow_ image memory.
Replacement for the ImageGrab_ Module, which works on Windows only.
For handling image memory (e.g. saving to file, converting,..) please read PIL_ or Pillow_ documentation.

Links:
 * home: https://github.com/ponty/pyscreenshot
 * documentation: http://ponty.github.com/pyscreenshot

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
 * supported python versions: 2.6, 2.7, 3.2, 3.3, 3.4
 * Plugin based, it has wrappers for various back-ends:
     * scrot_
     * ImageMagick_
     * PyGTK_
     * PIL_ or Pillow_ (only on windows)
     * PyQt4_
     * wxPython_
     * Quartz (Mac)
     * screencapture (Mac)

Known problems:
 * different back-ends generate slightly different images from the same desktop,
   this should be investigated
 * ImageMagick_ creates blackbox_ on some systems
 * PyGTK_ back-end does not check $DISPLAY -> not working with Xvfb
 * slow: 0.2s - 0.7s

Similar projects:
 - http://sourceforge.net/projects/gtkshots/
 - http://pypi.python.org/pypi/autopy


Examples
========

grab and show the whole screen ::
  
  # <== include('examples/showgrabfullscreen.py')==>
  from entrypoint2 import entrypoint
  from pyscreenshot import grab


  @entrypoint
  def show(backend='auto'):
      if backend == 'auto':
          backend = None
      im = grab(bbox=(100, 200, 300, 400), backend=backend)
      im.show()
  # <==end==>

to start the example:: 

    python -m pyscreenshot.examples.showgrabfullscreen

grab and show the part of the screen ::

  # <== include('examples/showgrabbox.py')==>
  from entrypoint2 import entrypoint
  from pyscreenshot import grab


  @entrypoint
  def show(backend='auto'):
      if backend == 'auto':
          backend = None
      im = grab(bbox=(100, 200, 300, 400), backend=backend)
      im.show()
  # <==end==>

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

Ubuntu
------
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
---------
::

    # as root
    pip uninstall pyscreenshot


Command line interface
======================

Back-end performance::

  # <== sh('python -m pyscreenshot.check.speedtest')==>

  n=10	 to_file: True	 bounding box: None
  ------------------------------------------------------
  Forced backend not found, or cannot be loaded:pil
  scrot               	1.5  sec	(  145 ms per call)
  wx                  	1.4  sec	(  138 ms per call)
  pygtk               	1.7  sec	(  165 ms per call)
  pyqt                	1.1  sec	(  112 ms per call)
  imagemagick         	6.1  sec	(  610 ms per call)
  Forced backend not found, or cannot be loaded:mac_screencapture
  Forced backend not found, or cannot be loaded:mac_quartz

  n=10	 to_file: False	 bounding box: None
  ------------------------------------------------------
  Forced backend not found, or cannot be loaded:pil
  scrot               	1.5  sec	(  152 ms per call)
  wx                  	0.19 sec	(   18 ms per call)
  pygtk               	1.7  sec	(  166 ms per call)
  pyqt                	1    sec	(  101 ms per call)
  imagemagick         	6    sec	(  604 ms per call)
  Forced backend not found, or cannot be loaded:mac_screencapture
  Forced backend not found, or cannot be loaded:mac_quartz

  n=10	 to_file: False	 bounding box: (10, 10, 20, 20)
  ------------------------------------------------------
  Forced backend not found, or cannot be loaded:pil
  scrot               	1.9  sec	(  186 ms per call)
  wx                  	0.19 sec	(   18 ms per call)
  pygtk               	0.0047 sec	(    0 ms per call)
  pyqt                	1.4  sec	(  135 ms per call)
  imagemagick         	4.5  sec	(  449 ms per call)
  Forced backend not found, or cannot be loaded:mac_screencapture
  Forced backend not found, or cannot be loaded:mac_quartz
  # <==end==>


Print versions::

  # <== sh('python -m pyscreenshot.check.versions')==>
  pyscreenshot         0.3.4
  pil                  missing
  scrot                0.8
  wx                   2.8.12.1
  pygtk                2.28.6
  pyqt                 not implemented
  imagemagick          6.7.7
  mac_screencapture    missing
  mac_quartz           missing
  # <==end==>


command line help
=================

::

  # <== sh('python -m pyscreenshot.check.speedtest --help')==>
  usage: speedtest.py [-h] [--debug]

  optional arguments:
    -h, --help  show this help message and exit
    --debug     set logging level to DEBUG
  # <==end==>

::

  # <== sh('python -m pyscreenshot.check.versions --help')==>
  usage: versions.py [-h] [--debug]

  optional arguments:
    -h, --help  show this help message and exit
    --debug     set logging level to DEBUG
  # <==end==>



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
.. |Travis| image:: http://img.shields.io/travis/ponty/pyscreenshot.svg
   :target: https://travis-ci.org/ponty/pyscreenshot/
.. |Coveralls| image:: http://img.shields.io/coveralls/ponty/pyscreenshot/master.svg
   :target: https://coveralls.io/r/ponty/pyscreenshot/
.. |Latest Version| image:: https://pypip.in/version/pyscreenshot/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |Supported Python versions| image:: https://pypip.in/py_versions/pyscreenshot/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |License| image:: https://pypip.in/license/pyscreenshot/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |Downloads| image:: https://pypip.in/download/pyscreenshot/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pyscreenshot/
.. |Code Health| image:: https://landscape.io/github/ponty/pyscreenshot/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ponty/pyscreenshot/master
.. |Documentation| image:: https://readthedocs.org/projects/pyscreenshot/badge/?version=latest
   :target: https://readthedocs.org/projects/pyscreenshot/?badge=latest
