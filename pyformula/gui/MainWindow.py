import pyformula
try:
    from PySide import QtCore, QtGui
    from PySide.QtCore import Signal, Slot, QFile
    from PySide.QtUiTools import QUiLoader
except ImportError:
    raise pyformula.PySideImportError


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = pyformula.gui.load_ui(pyformula.gui.get_ui_path(__file__))
