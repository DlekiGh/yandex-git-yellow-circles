import sys

from random import randint  # for randomised colors
from PyQt5.QtWidgets import QMainWindow, QApplication  # for QT app itself
from PIL import Image, ImageDraw  # for all th image manipulation
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        self.circles_canvas_label = QtWidgets.QLabel(Form)
        self.circles_canvas_label.setGeometry(QtCore.QRect(0, 0, 501, 501))
        self.circles_canvas_label.setText("")
        self.circles_canvas_label.setObjectName("circles_canvas_label")
        self.circles_pushButton = QtWidgets.QPushButton(Form)
        self.circles_pushButton.setGeometry(QtCore.QRect(170, 200, 151, 81))
        self.circles_pushButton.setObjectName("circles_pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Git и желтые окружности"))
        self.circles_pushButton.setText(_translate("Form", "баттн"))


class GitNYellowCircles(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.circles_pushButton.clicked.connect(self.draw_new_circle)

        self.img = Image.new('RGB', (500, 500), (255, 255, 255))
        self.circles_canvas_label.setPixmap(self.img.toqpixmap())
        self.ctx = ImageDraw.Draw(self.img)

        # main color and deviation range initialization for the drawn circles
        # yes, the main color is yandex color x3
        # deviation is set in int percent
        self.main_color = (255, 204, 0)
        self.color_deviation_range = 100

    # this method is called when the main button is clicked
    # the method draws a single circle on the canvas label
    def draw_new_circle(self):
        deviation = randint(-self.color_deviation_range, self.color_deviation_range)
        red, green, blue = self.main_color
        # adjust colors according to the generated percent
        color = (red + (255 - red) * deviation // 100,
                 green + (255 - green) * deviation // 100,
                 blue + (255 - blue) * deviation // 100)
        diameter = randint(50, 170)
        # generate such position that does not cut a part of the circle
        position = (randint(0, 500 - diameter), randint(0, 500 - diameter))
        xy = (position[0], position[1], position[0] + diameter, position[1] + diameter)
        self.ctx.ellipse(xy, outline=color, fill=None, width=6)
        self.circles_canvas_label.setPixmap(self.img.toqpixmap())


app = QApplication(sys.argv)
ex = GitNYellowCircles()
ex.show()
sys.exit(app.exec_())
