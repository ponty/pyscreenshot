#!/bin/bash
DISTRO=$1
PY=$2
# Ubuntu 14.04.6 LTS (Trusty Tahr)
# Ubuntu 16.04.6 LTS (Xenial Xerus)
# Ubuntu 18.04.3 LTS (Bionic Beaver)
# Ubuntu 20.04 LTS (Focal Fossa)

# no python3-wx before bionic
# no pyqt5 before xenial
# pygdk3 plugin is not compatible with trusty
# no python3-pyside before xenial
# no python-pyside2, python3-pyside2 before disco (19.04)
U1404_PY2="                          python-wxgtk2.8  python-qt4                    python-pyside  "  
U1604_PY2="python-gi  gir1.2-gtk-3.0 python-wxgtk3.0  python-qt4     python-pyqt5   python-pyside  "  
U1804_PY2="python-gi  gir1.2-gtk-3.0 python-wxgtk3.0  python-qt4     python-pyqt5   python-pyside  "  
U2004_PY2="python-gi  gir1.2-gtk-3.0 python-wxgtk3.0                                               "  

U1604_PY3="python3-gi gir1.2-gtk-3.0                  python3-pyqt4  python3-pyqt5  python3-pyside " 
U1804_PY3="python3-gi gir1.2-gtk-3.0 python3-wxgtk4.0 python3-pyqt4  python3-pyqt5  python3-pyside " 
U2004_PY3="python3-gi gir1.2-gtk-3.0 python3-wxgtk4.0                python3-pyqt5                 python3-pyside2.qtwidgets " 

if [[ ${DISTRO} == "trusty" ]];then
    if [[ ${PY} == "2" ]];then
        echo ${U1404_PY2}
    fi
    # if [[ ${PY} == "3" ]];then
    # fi
fi
if [[ ${DISTRO} == "xenial" ]];then
    if [[ ${PY} == "2" ]];then
        echo ${U1604_PY2}
    fi
    if [[ ${PY} == "3" ]];then
        echo ${U1604_PY3}
    fi
fi
if [[ ${DISTRO} == "bionic" ]];then
    if [[ ${PY} == "2" ]];then
        echo ${U1804_PY2}
    fi
    if [[ ${PY} == "3" ]];then
        echo ${U1804_PY3}
    fi
fi
if [[ ${DISTRO} == "focal" ]];then
    if [[ ${PY} == "2" ]];then
        echo ${U2004_PY2}
    fi
    if [[ ${PY} == "3" ]];then
        echo ${U2004_PY3}
    fi
fi


