import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle.ui', self)
        self.ok_pressed = False
        self.pushButton.clicked.connect(self.drawing)

    def paintEvent(self, event):
        if self.ok_pressed:
            painter = QPainter()
            painter.begin(self)
            x, y = random.randint(50, self.size().width()), random.randint(50, self.size().height())
            painter.setBrush(QColor(255, 220, 0))
            painter.setPen(QColor(255, 220, 0))
            d = random.randint(50, 200)
            painter.drawEllipse(x, y, d, d)
            painter.end()

    def drawing(self):
        self.ok_pressed = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleDrawer()
    ex.show()
    sys.exit(app.exec())
