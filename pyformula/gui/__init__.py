import os
from os.path import basename, splitext, join
import pyformula
try:
    from PySide import QtCore, QtGui
    from PySide.QtCore import Signal, Slot, QFile
    from PySide.QtUiTools import QUiLoader
except ImportError:
    raise pyformula.PySideImportError

def get_ui_path(py_filename):
    """Transforms a "/path/to/filename.py" string into a "/path/to/
    filename.ui" string, where the path is predefined in pyformula.paths.
    """
    ui_basename = "{}.ui".format(splitext(basename(py_filename))[0])
    return join(pyformula.paths['designer'], ui_basename)

def load_ui(ui_filename):
    """Returns an instance of a UI widget that is loaded in from a .ui file."""
    ui_file = QFile(ui_filename)
    loader = QUiLoader()
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui

from .MainWindow import MainWindow
