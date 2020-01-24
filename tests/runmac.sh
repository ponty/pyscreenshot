#!/bin/bash
set -e
nosetests -v  \
    test_def.py     \
    test_pil.py     \
    test_mac_quartz.py      \
    test_mac_screencapture.py   \
    test_pyqt5.py       \
    test_pyside2.py     \
    test_qtpy.py \
    easy
    
# nosetests -v test_pygdk3_conflict.py
# nosetests -v test_scrot.py
# nosetests -v test_imagemagick.py # TODO
# nosetests -v test_pyqt4.py
# nosetests -v test_pyside.py
# nosetests -v test_wx.py # TODO
# nosetests -v test_pygdk3.py # TODO
# nosetests -v test_pygtk.py
#nosetests -v test_gnome_screenshot.py

