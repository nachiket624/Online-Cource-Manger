from PySide2 import QtWidgets
from addresourceui import Ui_Dialog
import sys

fileloactionlist = []


class AddResorceDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(AddResorceDialog, self).__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        f1 = []
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            f1.append(f)
        fileloactionlist.extend(f1)
        fileloaction = tuple(fileloactionlist)
        print(fileloaction)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = AddResorceDialog()
    window.show()
    app.exec_()