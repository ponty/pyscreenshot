# -*- Import: -*-
from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages

try:
    # Optional tasks, only needed for development
    # -*- Optional import: -*-
    import paver.doctools
    import paver.virtual
    import paver.misctasks
    ALL_TASKS_LOADED = True
except ImportError, e:
    info("some tasks could not not be imported.")
    debug(str(e))
    ALL_TASKS_LOADED = False


#sys.path.append(path('.').abspath())
#from pyscreenshot import version
#ver = version.__version__
ver = '0.1.3'

classifiers = [
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ]

install_requires = [
    # -*- Install requires: -*-
    'setuptools',
    'yapsy',
    'path.py',
    'PIL',
    ]

entry_points = """
    # -*- Entry points: -*-
    """

# compatible with distutils of python 2.3+ or later
setup(
    name='pyscreenshot',
    version=ver,
    description='screenshot',
    long_description=open('README.rst', 'r').read(),
    classifiers=classifiers,
    keywords='screenshot',
    author='ponty',
    #author_email='zy@gmail.com',
    url='https://github.com/ponty/pyscreenshot',
    license='BSD',
    packages=find_packages(exclude=['bootstrap', 'pavement', ]),
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=False,
    install_requires=install_requires,
    entry_points=entry_points,
    )

options(
    # -*- Paver options: -*-
    minilib=Bunch(
        extra_files=[
            # -*- Minilib extra files: -*-
            ]
        ),
#    sphinx=Bunch(
#        docroot='docs',
#        builddir="_build",
#        sourcedir=""
#        ),
    virtualenv=Bunch(
        packages_to_install=[
            # -*- Virtualenv packages to install: -*-
            "nose",
            "Sphinx>=0.6b1",
            "pkginfo",
            "virtualenv"],
        dest_dir='./virtual-env/',
        install_paver=True,
        script_name='bootstrap.py',
        paver_command_line=None
        ),
    )

options.setup.package_data = paver.setuputils.find_package_data(
    'pyscreenshot', package='pyscreenshot', only_in_packages=False)

if ALL_TASKS_LOADED:
    @task
    @needs('generate_setup', 'minilib', 'setuptools.command.sdist')
    def sdist():
        """Overrides sdist to make sure that our setup.py is generated."""

@task
def pychecker():
    sh('pychecker --stdlib --only --limit 100 pyscreenshot/*.py')

@task
def findimports():
    '''list external imports
    sudo pip install findimports
    '''
    sh('findimports pyscreenshot |grep -v ":"|grep -v pyscreenshot|sort|uniq')

@task
def pyflakes():
    sh('pyflakes pyscreenshot')



