============
pyscreenshot
============

The ``pyscreenshot`` module can be used to copy 
the contents of the screen to a PIL_ image memory or file.
Replacement for the ImageGrab_ Module, which works on Windows only.

Plugin based, it has wrappers for scrot, ImageMagick_ and PIL_.

home: https://github.com/ponty/pyscreenshot

Usage
------------

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
------------

The easiest way to get pyscreenshot is if you have setuptools_ installed::

    easy_install https://github.com/ponty/pyscreenshot/zipball/master

or if you have pip_ installed::

    pip install https://github.com/ponty/pyscreenshot/zipball/master

Uninstall
---------

    pip uninstall pyscreenshot



.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _ImageGrab: http://www.pythonware.com/library/pil/handbook/imagegrab.htm
.. _PIL: http://www.pythonware.com/library/pil/
.. _ImageMagick: http://www.imagemagick.org/script/index.php
