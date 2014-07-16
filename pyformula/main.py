import sys
from PySide import QtGui
from . import __version__
from .gui.MainWindow import MainWindow


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationVersion(__version__)
    app.setApplicationName(app.tr("PyFomula"))

    form = MainWindow()
    form.show()

    app.exec_()
