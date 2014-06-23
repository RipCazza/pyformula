import os
from os.path import basename, splitext, join
import pyformula
from .MainWindow import MainWindow
try:
    from PySide import QtCore, QtGui
    from PySide.QtCore import Signal, Slot, QFile
    from PySide.QtUiTools import QUiLoader
except ImportError:
    raise pyformula.PySideImportError

def get_ui_path(py_filename):
    ui_basename = "{}.ui".format(splitext(basename(py_filename))[0])
    return join(pyformula.paths['designer'], ui_basename)

def load_ui(ui_filename):
    ui_file = QFile(ui_filename)
    loader = QUiLoader()
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui
