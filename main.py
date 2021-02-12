import random
import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.setup_ui()

    def setup_ui(self):
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle("Git и желтые окружности")
        self.button.clicked.connect(self.redraw_circles)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        color = QtGui.QColor(255, 255, 0)
        painter.setBrush(QtGui.QBrush(color, Qt.SolidPattern))
        for circle in self.circles:
            painter.drawEllipse(*circle)

    def redraw_circles(self):
        size = random.randint(50, 200)
        self.circles.append((random.randint(10, 300),
                             random.randint(10, 300), size, size))
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
