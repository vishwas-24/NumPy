# PyQt5 buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(600, 400, 800, 500)
        self.setWindowIcon(QIcon(r"C:\Users\vishw\OneDrive\Pictures\Loki pfp.jpg"))
        self.button = QPushButton("Click me!", self)
        self.lable = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(300, 150, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.lable.setGeometry(350, 50, 200, 100)
        self.lable.setStyleSheet("font-size: 30px;")

    def on_click(self):
        # print("Button clicked!")
        self.button.setText("Clicked!")
        self.lable.setText("Goodbye!")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()