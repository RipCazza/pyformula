import os
import pyformula
from .MainWindow import MainWindow
try:
    from PySide import QtCore, QtGui
    from PySide.QtCore import Signal, Slot, QFile
    from PySide.QtUiTools import QUiLoader
except ImportError:
    raise pyformula.PySideImportError

def loadUi(py_filename):
    ui_file = QFile(os.path.join(pyformula.paths['designer'],
        "{}.ui".format(py_filename[:-len(".py")])))
    loader = QUiLoader()
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui
