#!/bin/bash
DISTRO=$1
# Ubuntu 14.04.6 LTS (Trusty Tahr)
# Ubuntu 16.04.6 LTS (Xenial Xerus)
# Ubuntu 18.04.3 LTS (Bionic Beaver)
# Ubuntu 20.04 LTS (Focal Fossa)

# no python3-wx before bionic
# no pyqt5 before xenial
# pygdk3 plugin is not compatible with trusty
# no python3-pyside before xenial
# no python3-pyside2 before disco (19.04)
U1604_PY3="python3-gi gir1.2-gtk-3.0                  python3-pyqt4  python3-pyqt5  python3-pyside " 
U1804_PY3="python3-gi gir1.2-gtk-3.0 python3-wxgtk4.0 python3-pyqt4  python3-pyqt5  python3-pyside " 
U2004_PY3="python3-gi gir1.2-gtk-3.0 python3-wxgtk4.0                python3-pyqt5                 python3-pyside2.qtwidgets " 

if [[ ${DISTRO} == "xenial" ]];then
    echo ${U1604_PY3}
fi
if [[ ${DISTRO} == "bionic" ]];then
    echo ${U1804_PY3}
fi
if [[ ${DISTRO} == "focal" ]];then
    echo ${U2004_PY3}
fi


