import sys
from PySide import QtCore, QtGui
from ..formulae import guided


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self._init_ui()
        self.fill_function_combo()
        self.refresh_function_switch()
        self.refresh_input_widget()

        self.function_combo.currentIndexChanged.connect(
            self.refresh_function_switch)
        self.function_combo.currentIndexChanged.connect(
            self.refresh_input_widget)
        self.function_combo.currentIndexChanged.connect(
            self.answer_lbl.clear)
        self.calc_btn.clicked.connect(self.calc)

    def _init_ui(self):
        self.central_widget = QtGui.QWidget(self)
        self.setCentralWidget(self.central_widget)

        function_layout = QtGui.QHBoxLayout()
        self.function_lbl = QtGui.QLabel(self.tr("Functie:"))
        self.function_combo = QtGui.QComboBox()
        function_layout.addWidget(self.function_lbl)
        function_layout.addWidget(self.function_combo)

        desc_layout = QtGui.QHBoxLayout()
        self.desc_lbl = QtGui.QLabel()
        self.desc_lbl.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        desc_layout.addWidget(self.desc_lbl)

        # To be filled depending on selected function.
        input_layout = QtGui.QVBoxLayout()
        self.input_widget = QtGui.QStackedWidget()
        #self.input_widget.setSizePolicy(QtGui.QSizePolicy.Preferred,
                                        #QtGui.QSizePolicy.Fixed)
        input_layout.addWidget(self.input_widget)

        calc_layout = QtGui.QHBoxLayout()
        self.calc_btn = QtGui.QPushButton(self.tr("Bereken"))
        calc_layout.addStretch()
        calc_layout.addWidget(self.calc_btn)

        answer_layout = QtGui.QVBoxLayout()
        self.answer_lbl = QtGui.QLabel()
        self.answer_lbl.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        answer_layout.addWidget(self.answer_lbl)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(function_layout)
        layout.addLayout(desc_layout)
        layout.addLayout(input_layout)
        layout.addLayout(calc_layout)
        layout.addStretch()
        layout.addLayout(answer_layout)
        self.central_widget.setLayout(layout)

    def fill_function_combo(self):
        # We'll have to manually add all functions here.  It's a shit solution,
        # but it's the best we've got.
        self.function_combo.addItem(guided.abc.name, guided.abc)
        self.function_combo.addItem(guided.exponential_sum.name,
                                    guided.exponential_sum)
        self.function_combo.addItem(guided.value_percentage.name,
                                    guided.value_percentage)
        self.function_combo.addItem(guided.percentage_new_value.name,
                                    guided.percentage_new_value)
        self.function_combo.addItem(guided.percentage_orig_value.name,
                                    guided.percentage_orig_value)
        self.function_combo.addItem(guided.exponential_growth_total.name,
                                    guided.exponential_growth_total)
        self.function_combo.addItem(guided.exponential_growth_base.name,
                                    guided.exponential_growth_base)
        self.function_combo.addItem(guided.pythagoras_diagonal.name,
                                    guided.pythagoras_diagonal)
        self.function_combo.addItem(guided.pythagoras_rectangular.name,
                                    guided.pythagoras_rectangular)
        self.function_combo.addItem(guided.tangens_radian.name,
                                    guided.tangens_radian)
        self.function_combo.addItem(guided.sinus_radian.name,
                                    guided.sinus_radian)
        self.function_combo.addItem(guided.cosinus_radian.name,
                                    guided.cosinus_radian)
        self.function_combo.addItem(guided.tangens_o.name,
                                    guided.tangens_o)
        self.function_combo.addItem(guided.sinus_o.name,
                                    guided.sinus_o)
        self.function_combo.addItem(guided.cosinus_a.name,
                                    guided.cosinus_a)
        self.function_combo.addItem(guided.tangens_a.name,
                                    guided.tangens_a)
        self.function_combo.addItem(guided.sinus_s.name,
                                    guided.sinus_s)
        self.function_combo.addItem(guided.cosinus_s.name,
                                    guided.cosinus_s)

    def refresh_function_switch(self):
        index = self.function_combo.currentIndex()
        function = self.function_combo.itemData(index)

        self.desc_lbl.setText(function.expr)

    def refresh_input_widget(self):
        index = self.function_combo.currentIndex()
        function = self.function_combo.itemData(index)

        self.input_widget.addWidget(InputWidget(function))
        self.input_widget.setCurrentIndex(self.input_widget.count()-1)

    def calc(self):
        args = {}

        for key, spin in self.input_widget.currentWidget().spins.items():
            args[key] = spin.value()

        index = self.function_combo.currentIndex()
        function = self.function_combo.itemData(index)

        try:
            instructions = function(args)
        except:
            self.answer_lbl.setText(self.tr("Geen oplossing gevonden"))
            return

        text = ""

        for instruction in instructions:
            text += "<p>" + instruction.orig_func + "<br>\n"
            text += instruction.filled_in_func + "</p>\n\n"
            #text = text + instruction.ans + "\n"

        text +=  "<p><b>" + instructions[-1].ans + "</b></p>"

        self.answer_lbl.setText(text)

class InputWidget(QtGui.QWidget):
    def __init__(self, function):
        super(InputWidget, self).__init__()

        self.spins = {}

        layout = QtGui.QVBoxLayout()

        for arg in function.args:
            hor_layout = QtGui.QHBoxLayout()
            label = QtGui.QLabel("{}:".format(arg))
            label.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                QtGui.QSizePolicy.Fixed)
            dspinbox = QtGui.QDoubleSpinBox()
            dspinbox.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Fixed)
            dspinbox.setMaximum(sys.maxsize)
            dspinbox.setMinimum(-sys.maxsize - 1)
            hor_layout.addWidget(label)
            hor_layout.addWidget(dspinbox)

            layout.addLayout(hor_layout)

            self.spins[arg] = dspinbox

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
