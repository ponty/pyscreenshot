#!/bin/bash
DIST=$1
set -e
#sleep 1

TESTS="test_scrot.py test_imagemagick.py test_def.py"

if [[ ${DIST} != "general" ]];then
    PYTHON_VERSION=$2
    PY=${PYTHON_VERSION:0:1}
    if [[ ${DIST} != "trusty" ]];then
        TESTS="${TESTS} test_pygdk3.py test_pyqt5.py"
    fi
    if [[ ${DIST} != "xenial" ]];then
    if [[ ${PY} == "2" ]];then
        TESTS="${TESTS} test_wx.py"
    fi
    fi
    TESTS="${TESTS} test_pyqt4.py test_pyside.py"
    if [[ ${PY} == "2" ]];then
        TESTS="${TESTS} test_pygtk.py"
    fi

    if [[ ${DIST} == "bionic" ]];then
        TESTS="${TESTS} test_qtpy.py test_pyside2.py"
    fi
fi


#nosetests -v test_gnome_screenshot.py
#nosetests -v test_mac_quartz.py
#nosetests -v test_mac_screencapture.py

nosetests -v  ${TESTS} easy


