#!/bin/bash
set -e

rm /tmp/fillscreen.bmp || true
python3 fillscreen.py &
FILL_PID=$!
while [ ! -f /tmp/fillscreen.bmp ]; do sleep 1; done

#sleep 5

nosetests -v test_def.py
# nosetests -v test_pygdk3_conflict.py
# nosetests -v test_scrot.py
# nosetests -v test_imagemagick.py # TODO
# nosetests -v test_pyqt4.py
nosetests -v test_pyqt5.py
# nosetests -v test_pyside.py
nosetests -v test_pyside2.py
nosetests -v test_qtpy.py
# nosetests -v test_wx.py # TODO
# nosetests -v test_pygdk3.py # TODO
# nosetests -v test_pygtk.py

#nosetests -v test_gnome_screenshot.py
nosetests -v test_pil.py
nosetests -v test_mac_quartz.py
nosetests -v test_mac_screencapture.py

nosetests -v easy

kill $FILL_PID
