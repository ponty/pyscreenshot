import os.path

from setuptools import setup

NAME = "pyscreenshot"

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__


URL = "https://github.com/ponty/pyscreenshot"
DESCRIPTION = "python screenshot"
LONG_DESCRIPTION = """The pyscreenshot module is obsolete in most cases. 
It was created because PIL ImageGrab module worked on Windows only,
but now Linux and macOS are also supported.
There are some features in pyscreenshot which can be useful in special cases:
flexible backends, Wayland support, sometimes better performance, optional subprocessing.

The module can be used to copy the contents of the screen to a Pillow image memory using various back-ends. Replacement for the ImageGrab Module.

Documentation: https://github.com/ponty/pyscreenshot/tree/"""
LONG_DESCRIPTION += VERSION

PACKAGES = [
    NAME,
    NAME + ".plugins",
    NAME + ".check",
    NAME + ".cli",
    NAME + ".examples",
]

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]

install_requires = [
    "EasyProcess",
    "entrypoint2",
    "mss ; python_version > '3.4'",
    "jeepney ; python_version > '3.4' and platform_system == 'Linux'",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    python_requires=">=3.4",
    classifiers=classifiers,
    keywords="screenshot",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    #     include_package_data=True,
    #     zip_safe=False,
    install_requires=install_requires,
    # **extra
)
