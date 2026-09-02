# PyQt5 images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(600, 400, 800, 500)
        self.setWindowIcon(QIcon(r"C:\Users\vishw\OneDrive\Pictures\Loki pfp.jpg"))

        lable = QLabel(self)
        lable.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap(r"C:\Users\vishw\OneDrive\Pictures\Loki pfp.jpg")
        lable.setPixmap(pixmap)

        lable.setScaledContents(True)

        # lable.setGeometry(0, 0, lable.width(), lable.height())
        lable.setGeometry((self.width() - lable.width()) // 2, 
                          (self.height() - lable.height()) // 2,    # // is integer division
                          lable.width(),
                          lable.height())

class main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()