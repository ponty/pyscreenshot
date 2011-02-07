============
pyscreenshot
============

The ``pyscreenshot`` module can be used to copy
the contents of the screen to a PIL_ image memory or file.
Replacement for the ImageGrab_ Module, which works on Windows only.

Plugin based, it has wrappers for scrot, ImageMagick_, PyGTK_ and PIL_.

(ImageMagick_ creates blackbox_ on some systems)

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

You should install at least one backend on linux.

On Ubuntu::

    # Python Imaging Library (required)
    sudo apt-get install python-imaging

    # one of them
    sudo apt-get install scrot
    sudo apt-get install imagemagick
    sudo apt-get install python-gtk2

The easiest way to get pyscreenshot is if you have setuptools_ installed::

    easy_install pyscreenshot

or if you have pip_ installed::

    pip install pyscreenshot

Uninstall::

    pip uninstall pyscreenshot


Speed
======

::

    n=10 to_file: True bounding box: None
    ------------------------------------------------------
    scrot       2.2 sec
    imagemagick 5.2 sec
    pygtk       3.2 sec

    n=10 to_file: False bounding box: None
    ------------------------------------------------------
    scrot       2.1 sec
    imagemagick 5.2 sec
    pygtk       3.2 sec

    n=10 to_file: False bounding box: (10, 10, 20, 20)
    ------------------------------------------------------
    scrot       2.6 sec
    imagemagick 1.9 sec
    pygtk       3.6 sec



.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _ImageGrab: http://www.pythonware.com/library/pil/handbook/imagegrab.htm
.. _PIL: http://www.pythonware.com/library/pil/
.. _ImageMagick: http://www.imagemagick.org/
.. _PyGTK: http://www.pygtk.org/
.. _blackbox: http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=13658
