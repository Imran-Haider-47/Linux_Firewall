from PyQt6.QtWidgets import QMainWindow, QDialog
from addRule2 import add_rule_Dialog
from simple_firewall import Simple_Firewall_Dialog
from about_us import Ui_Dialog_About_Us
from help import Ui_Dialog_help
from profile import Ui_Dialog_profile
from MainPage import Ui_MainWindow
class Firewall(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_Rules.clicked.connect(self.add_rule)
        self.toolButton_Firewall.clicked.connect(self.simple_firewall)
        self.toolButton_About.clicked.connect(self.about_us)
        self.toolButton_help.clicked.connect(self.help)
        self.pushButton_Profile.clicked.connect(self.profile)

    def simple_firewall(self):
        dialog = QDialog()
        ui = Simple_Firewall_Dialog()
        ui.setupUi(dialog)
        dialog.exec()
    def add_rule(self):
        dialog = QDialog()
        ui = add_rule_Dialog()

        ui.setupUi(dialog)
        dialog.exec()
    def about_us(self):
        dialog = QDialog()
        ui = Ui_Dialog_About_Us()

        ui.setupUi(dialog)
        dialog.exec()
    def help(self):
        dialog = QDialog()
        ui = Ui_Dialog_help()

        ui.setupUi(dialog)
        dialog.exec()
    def profile(self):
        dialog = QDialog()
        ui = Ui_Dialog_profile()
        ui.setupUi(dialog)
        dialog.exec()






