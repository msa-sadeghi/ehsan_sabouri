from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from student_management import Ui_Dialog
from db import Database

class StudentForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.load_students()

    def load_students(self):
        db = Database()
        cur = db.cursor
        cur.execute("SELECT id, first_name, last_name,class_id FROM students ORDER BY id")
        rows = cur.fetchall()
     

        self.ui.tableWidget_students.setRowCount(0)
        for row_num, row in enumerate(rows):
            self.ui.tableWidget_students.insertRow(row_num)
           
            for col_num, data in dict(row).items():
                print(col_num, data)
                self.ui.tableWidget_students.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        