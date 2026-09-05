# PyQt5 line widgets/textbox 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(600, 400, 800, 500)
        self.setWindowIcon(QIcon(r"C:\Users\vishw\OneDrive\Pictures\Loki pfp.jpg"))
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter your name")
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;") 
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;") 
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello, {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()