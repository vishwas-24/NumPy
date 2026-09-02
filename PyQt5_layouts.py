# PyQt5 layouts

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(600, 400, 800, 500)
        self.setWindowIcon(QIcon(r"C:\Users\vishw\OneDrive\Pictures\Loki pfp.jpg"))
        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        lable1 = QLabel("#1", self)
        lable2 = QLabel("#2", self)
        lable3 = QLabel("#3", self)
        lable4 = QLabel("#4", self)
        lable5 = QLabel("#5", self)

        lable1.setStyleSheet("background-color: red;")
        lable2.setStyleSheet("background-color: yellow;")
        lable3.setStyleSheet("background-color: green;")
        lable4.setStyleSheet("background-color: blue;")
        lable5.setStyleSheet("background-color: purple;")

        # vbox = QVBoxLayout()      # for vertical line
        # hbox = QHBoxLayout()      # for horizontal line
        grid = QGridLayout()        # for grid type layout

        # vbox.addWidget(lable1)
        # vbox.addWidget(lable2)
        # vbox.addWidget(lable3)
        # vbox.addWidget(lable4)
        # vbox.addWidget(lable5)

        # hbox.addWidget(lable1)
        # hbox.addWidget(lable2)
        # hbox.addWidget(lable3)
        # hbox.addWidget(lable4)
        # hbox.addWidget(lable5)

        grid.addWidget(lable1, 0, 0)
        grid.addWidget(lable2, 0, 1)
        grid.addWidget(lable3, 1, 0)
        grid.addWidget(lable4, 1, 1)
        grid.addWidget(lable5, 2, 0)
        # central_widget.setLayout(vbox)
        # central_widget.setLayout(hbox)
        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()