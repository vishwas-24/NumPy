# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt     # used for alignmentes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(600, 400, 800, 500)
        self.setWindowIcon(QIcon(r"C:\Users\vishw\OneDrive\Pictures\Loki pfp.jpg"))
        lable = QLabel("Hello", self)
        lable.setFont(QFont("Arial", 30))
        lable.setGeometry(0, 0, 500, 400)
        # lable.setStyleSheet("color: red;")
        lable.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # lable.setAlignment(Qt.AlignTop)      # Vertically Top
        # lable.setAlignment(Qt.AlignBottom)   # Vertically Bottom
        # lable.setAlignment(Qt.AlignVCenter)  # Vertically Center
        # lable.setAlignment(Qt.AlignRight)    # Horizontally Right
        # lable.setAlignment(Qt.AlignHCenter)    # Horizontally Center
        # lable.setAlignment(Qt.AlignCenter)
        # lable.setAlignment(Qt.AlignHCenter | Qt.AlignTop) 
        lable.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()