from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from login_form import Ui_Dialog


class LoginForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == "admin" and password == "1234":
            # QMessageBox.information(self, "welcome", "login success")
            self.accept()
        else:
            QMessageBox.information(self, "error", "login not success")
