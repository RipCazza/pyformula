import os
from os.path import basename, splitext, join
import pyformula
try:
    from PySide import QtCore, QtGui
    from PySide.QtCore import Signal, Slot, QFile
    from PySide.QtUiTools import QUiLoader
except ImportError:
    raise pyformula.PySideImportError


class MyQUiLoader(QUiLoader):
    """Re-implemented QUiLoader.

    See:
    github.com/lunaryorn/snippets/blob/master/qt4/designer/pyside_dynamic.py


    """
    def __init__(self, baseinstance):
        QUiLoader.__init__(self, baseinstance)
        self.baseinstance = baseinstance

    def createWidget(self, class_name, parent=None, name=""):
        if parent is None and self.baseinstance:
            return self.baseinstance
        else:
            widget = QUiLoader.createWidget(self, class_name, parent, name)
            if self.baseinstance:
                setattr(self.baseinstance, name, widget)
            return widget

def get_ui_path(py_filename):
    """Transforms a "/path/to/filename.py" string into a "/path/to/
    filename.ui" string, where the path is predefined in pyformula.paths.
    """
    ui_basename = "{}.ui".format(splitext(basename(py_filename))[0])
    return join(pyformula.paths['designer'], ui_basename)

def load_ui(ui_filename, baseinstance=None):
    """Returns an instance of a UI widget that is loaded in from a .ui file.
    If baseinstance is an object, that object is altered. If baseinstance
    remains None, a new QWidget is returned.
    """
    loader = MyQUiLoader(baseinstance)
    ui = loader.load(ui_filename)
    QtCore.QMetaObject.connectSlotsByName(ui)
    return ui

from .MainWindow import MainWindow
