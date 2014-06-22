import os


class PySideImportError(Exception):
    pass

_basepath = os.path.dirname(os.path.dirname(__file__))

paths = {
          "designer" : os.path.join(_basepath, "designer"),
        }

try:
    from . import main
    from . import gui
except PySideImportError:
    print("PySide could not be imported"
from . import formulae

__authors__      = ["Stefan Bakker", "Jesse Zwitserlood", "Ruben Bakker"]
__author__       = ', '.join(__authors__)
__maintainer__   = "Stefan Bakker"
__email__        = "s.bakker777@gmail.com"
__version_info__ = (0, 0, 1, 'a',)  # Empty string if release version.
__version__      = "{0}.{1}.{2}{3}".format(__version_info__[0],
                                      __version_info__[1],
                                      __version_info__[2],
                                      __version_info__[3])
__license__      = "GNU GPLv3"
