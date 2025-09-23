from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from student_management import Ui_Dialog
from db import Database

class StudentForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = Database()
        self.load_students()
        self.ui.pushButton_add_student.clicked.connect(self.add_student)

    def load_students(self):
        self.db.execute("SELECT id, first_name, last_name,class_id FROM students ORDER BY id")
        rows = self.db.cursor.fetchall()
     

        self.ui.tableWidget_students.setRowCount(0)
        self.ui.tableWidget_students.setColumnCount(len(dict(rows[0]).keys()))
        self.ui.tableWidget_students.setHorizontalHeaderLabels(dict(rows[0]).keys())
        
        for row_num, row in enumerate(rows):
            self.ui.tableWidget_students.insertRow(row_num)
           
            col_index = 0
            for col_num, data in dict(row).items():
                self.ui.tableWidget_students.setItem(row_num, col_index, QTableWidgetItem(str(data)))
                col_index += 1
        

    def add_student(self):
        firstname = self.ui.lineEdit_firstname.text()
        lastname = self.ui.lineEdit_lastname.text()
        class_id = self.ui.lineEdit_classid.text()

        if not firstname or not lastname or not class_id:
            QMessageBox.warning(self, "خطا", "لطفا همه فیلدها را پر نمائید")
            return
        self.db.execute('INSERT INTO students(first_name, last_name, class_id) VALUES (%s, %s, %s)',
                        (firstname, lastname, class_id))
        
        self.load_students()
        
        self.ui.lineEdit_firstname.clear()
        self.ui.lineEdit_lastname.clear()
        self.ui.lineEdit_classid.clear()