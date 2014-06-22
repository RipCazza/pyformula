import pyformula
import os
try:
    from PySide import QtCore, QtGui
    from PySide.QtCore import Signal, Slot, QFile
    from PySide.QtUiTools import QUiLoader
except ImportError:
    raise pyformula.PySideImportError


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = pyformula.gui.loadUi(os.path.basename(__file__))
