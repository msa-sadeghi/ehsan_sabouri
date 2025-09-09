from PyQt5.QtWidgets import QApplication
from login_ui_form import LoginForm
from main_ui_form import MainWindow
app = QApplication([])
login = LoginForm()

if login.exec_() == LoginForm.Accepted:
    window = MainWindow()
    window.show()
    app.exec_()
