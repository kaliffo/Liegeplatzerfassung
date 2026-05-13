from Liegeplatzdaten import Ui_frmLiegeplatzerfassung
from PyQt6 import  QtWidgets
from PyQt6.QtWidgets import QApplication
import sys


class MainForm(QtWidgets.QWidget, Ui_frmLiegeplatzerfassung):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

    def btnSave_click(self):
        print("Saved")

    def btnNew_click(self):
        print("Created")

    def btnClose_click(self):
        print("Closed")
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec())
