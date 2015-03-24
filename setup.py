from setuptools import setup
import os.path
import sys


NAME = 'pyscreenshot'
URL = 'https://github.com/ponty/pyscreenshot'
DESCRIPTION = 'python screenshot'
PACKAGES = ['pyscreenshot',
            'pyscreenshot.plugins',
            'pyscreenshot.check',
            'pyscreenshot.examples',
            ]

# get __version__
__version__ = None
exec(open(os.path.join(NAME , 'about.py')).read())
VERSION = __version__

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    "Programming Language :: Python :: 2",
    #    "Programming Language :: Python :: 2.3",
    #    "Programming Language :: Python :: 2.4",
    #"Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    #    "Programming Language :: Python :: 2 :: Only",
#     "Programming Language :: Python :: 3",
    #    "Programming Language :: Python :: 3.0",
#     "Programming Language :: Python :: 3.1",
#     "Programming Language :: Python :: 3.2",
#     "Programming Language :: Python :: 3.3",
#     "Programming Language :: Python :: 3.4",
]

install_requires = ['EasyProcess']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.rst', 'r').read(),
    classifiers=classifiers,
    keywords='screenshot',
    author='ponty',
    # author_email='',
    url=URL,
    license='BSD',
    packages=PACKAGES,
#     include_package_data=True,
#     test_suite='nose.collector',
#     zip_safe=False,
    install_requires=install_requires,
    **extra
)
