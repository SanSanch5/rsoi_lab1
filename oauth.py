import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_ppAuthForm

class MyForm(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ppAuthForm()
        self.ui.setupUi(self)
        self.ui.lblAnsOpen.setText('')
        self.ui.lblAnsClose.setText('')
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        self.ui.funcOpenClick.clicked.connect(self.helloworld)

    def helloworld(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.lblAnsOpen.setText(_translate("ppAuthForm", "Открытая функция"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())