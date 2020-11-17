from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import Qt
import random
import sys


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.allow_paint = False
        self.setup_ui()

    def setup_ui(self):
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle("Git и желтые окружности")
        self.button.clicked.connect(self.set_paint_active)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        color = QtGui.QColor(255, 255, 0)
        size = random.randint(50, 200)
        painter.setBrush(QtGui.QBrush(color, Qt.SolidPattern))
        for _ in range(random.randint(1, 10)):
            painter.drawEllipse(random.randint(10, 300),
                                random.randint(10, 300), size, size)
        self.allow_paint = False

    def set_paint_active(self):
        self.allow_paint = True
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
