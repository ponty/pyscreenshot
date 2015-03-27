from paver.doctools import cog
from paver.easy import options
from paver.options import Bunch

EXPORTED_TASKS=[cog]
    
options(
    cog=Bunch(
        basedir='.',
        pattern='README.rst',
        includedir='pyscreenshot',
        beginspec='<==',
        endspec='==>',
        endoutput='<==end==>',
    )
)
