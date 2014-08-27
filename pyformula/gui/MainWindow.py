from PySide import QtCore, QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.central_widget = QtGui.QWidget(self)
        self.setCentralWidget(self.central_widget)

        function_layout = QtGui.QHBoxLayout()
        self.function_lbl = QtGui.QLabel(self.tr("Functie:"))
        self.function_combo = QtGui.QComboBox()
        function_layout.addWidget(self.function_lbl)
        function_layout.addWidget(self.function_combo)

        desc_layout = QtGui.QHBoxLayout()
        self.desc_lbl = QtGui.QLabel(self.tr("a = b * c"))
        desc_layout.addWidget(self.desc_lbl)

        # To be filled depending on selected function.
        self.input_layout = QtGui.QVBoxLayout()

        answer_layout = QtGui.QVBoxLayout()
        self.answer_lbl = QtGui.QLabel(self.tr("N/A"))
        answer_layout.addWidget(self.answer_lbl)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(function_layout)
        layout.addLayout(desc_layout)
        layout.addLayout(self.input_layout)
        layout.addLayout(answer_layout)
        self.central_widget.setLayout(layout)
