============
pyscreenshot
============

The ``pyscreenshot`` module can be used to copy
the contents of the screen to a PIL_ image memory or file.
Replacement for the ImageGrab_ Module, which works on Windows only.

Plugin based, it has wrappers for various backends:
 * scrot (recommended)
 * ImageMagick_ (it creates blackbox_ on some systems)
 * PyGTK_ (does not check $DISPLAY)
 * PIL_ (only on windows)

home: https://github.com/ponty/pyscreenshot

Usage
============

Example::

    import pyscreenshot as ImageGrab
    # fullscreen
    im=ImageGrab.grab()
    im.show()
    # part of the screen
    im=ImageGrab.grab(bbox=(10,10,500,500))
    im.show()
    # to file
    ImageGrab.grab_to_file('im.png')

Installation
============

General
--------

 * install setuptools_ or pip_
 * install PIL_
 * install at least one backend
 * install the program:

if you have setuptools_ installed::

    # as root
    easy_install pyscreenshot

if you have pip_ installed::

    # as root
    pip install pyscreenshot

Ubuntu
----------
::

    # one or more
    sudo apt-get install scrot
    sudo apt-get install imagemagick
    sudo apt-get install python-gtk2

    # Python Imaging Library (required)
    sudo apt-get install python-imaging

    sudo apt-get install python-setuptools
    sudo easy_install pyscreenshot

Uninstall
----------
::

    # as root
    pip uninstall pyscreenshot



.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _ImageGrab: http://www.pythonware.com/library/pil/handbook/imagegrab.htm
.. _PIL: http://www.pythonware.com/library/pil/
.. _ImageMagick: http://www.imagemagick.org/
.. _PyGTK: http://www.pygtk.org/
.. _blackbox: http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=13658
