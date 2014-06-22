import pyformula


try:
    from PySide import QtCore, QtGui, uic
    from PySide.QtCore import Signal, Slot
except ImportError:
    raise pyformula.PySideImportError

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_filename = "{}.ui".format(os.path.basename(__file__)[:-len(".py")])
        self.ui = uic.loadUi(os.path.join(pyformula.paths['designer'],
                                          ui_filename), self)

