import os.path

from setuptools import setup

NAME = "pyscreenshot"

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__


URL = "https://github.com/ponty/pyscreenshot"
DESCRIPTION = "python screenshot"
LONG_DESCRIPTION = """The pyscreenshot module can be used to copy the contents of the screen to a Pillow image memory using various back-ends. Replacement for the ImageGrab Module.

Documentation: https://github.com/ponty/pyscreenshot/tree/"""
LONG_DESCRIPTION += VERSION

PACKAGES = [
    NAME,
    NAME + ".plugins",
    NAME + ".check",
    NAME + ".cli",
    NAME + ".examples",
]


# extra = {}
# if sys.version_info >= (3,):
#     extra['use_2to3'] = True
#     extra['use_2to3_exclude_fixers'] = ['lib2to3.fixes.fix_import']

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
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
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
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
