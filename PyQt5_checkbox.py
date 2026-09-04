# PyQt5 checkbox

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(600, 400, 800, 500)
        self.setWindowIcon(QIcon(r"C:\Users\vishw\OneDrive\Pictures\Loki pfp.jpg"))
        self.checkbox = QCheckBox("Do you like Avengers?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;" 
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.on_checked)

    def on_checked(self, state):
        if state == Qt.Checked:
            print("You like Avengers!")
        else:
            print("You don't like Avengers!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()