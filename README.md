pyformula
=========
Small algebraic calculator app written in Python.

Requirements for Windows
=========

* Python 3.4  - https://www.python.org/download
* PySide      - `pip install pyside`
* SymPy       - `pip install sympy`
* Qt Designer - http://qt-project.org/downloads

Requirements for Linux
=========

* Python 3.4  - `sudo apt-get install python3`
* PySide      - `sudo apt-get install python3-pyside` OR `sudo pip3 install pyside`
* SymPy       - `sudo pip3 install sympy`
* Qt Designer - `sudo apt-get install qt4-designer`

Python 2 compatibility
=========

Python 2.7 technically works. It requires the 2.7 modules of PySide and SymPy.
The program has to be run with bytecode generation disabled, because
`os.path.basename(__file__)` would otherwise return `filename.pyc` instead of
`filename.py`, which is undesirable and crashes the program. `find - -name
"*.pyc" -delete` deletes all Python bytecode.`python -B script.py` runs the
a Python script without generating bytecode.

A more ideal solution would be to get the base name of the Python file without
the file extension suffix.
