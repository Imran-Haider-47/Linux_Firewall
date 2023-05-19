import sys
from PyQt6.QtWidgets import QApplication
from loginForm import Ui_LoginForm
from PyQt6 import QtWidgets
from Firwall import Firewall
app = QApplication(sys.argv)

firewall = Firewall()
LoginForm = QtWidgets.QWidget()
ui = Ui_LoginForm()
ui.setupUi(LoginForm)
LoginForm.show()

sys.exit(app.exec())