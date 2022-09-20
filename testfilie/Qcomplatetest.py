from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QCompleter

#
#


class Completer(QtWidgets.QCompleter):

    def __init__(self, parent=None):
        super(Completer, self).__init__(parent)

        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.setWrapAround(False)

    # Add texts instead of replace
    def pathFromIndex(self, index):
        path = QtWidgets.QCompleter.pathFromIndex(self, index)

        lst = str(self.widget().text()).split(',')

        if len(lst) > 1:
            path = '%s, %s' % (','.join(lst[:-1]), path)

        return path

    # Add operator to separate between texts
    def splitPath(self, path):
        path = str(path.split(',')[-1]).lstrip(' ')
        return [path]

class TextEdit(QtWidgets.QLineEdit):

    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)

        self.setPlaceholderText("example : ")
        self._completer = Completer(self)


        self.setCompleter(self._completer)

def main():
    app     = QApplication(sys.argv)
    edit    = QLineEdit()
    strList = ["Germany", "Spain", "France", "Norway"]
    completer = QCompleter(strList,edit)

    edit.setCompleter(completer)
    edit.show()

    sys.exit(app.exec_())
#
if __name__ == '__main__':
    main()