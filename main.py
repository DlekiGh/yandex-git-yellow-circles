import sys

from random import randint  # for randomised colors
from PyQt5.QtWidgets import QMainWindow, QApplication  # for QT app itself
from PyQt5 import uic  # first time using the thing
from PIL import Image, ImageDraw  # for all th image manipulation


class GitNYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.circles_pushButton.clicked.connect(self.draw_new_circle)

        self.img = Image.new('RGB', (500, 500), (255, 255, 255))
        self.circles_canvas_label.setPixmap(self.img.toqpixmap())
        self.ctx = ImageDraw.Draw(self.img)

        # yes, the main color is yandex color x3
        self.main_color = (255, 204, 0)

    # this method is called when the main button is clicked
    # the method draws a single circle on the canvas label
    def draw_new_circle(self):
        diameter = randint(50, 170)
        # generate such position that does not cut a part of the circle
        position = (randint(0, 500 - diameter), randint(0, 500 - diameter))
        xy = (position[0], position[1], position[0] + diameter, position[1] + diameter)
        self.ctx.ellipse(xy, outline=self.main_color, fill=None, width=6)
        self.circles_canvas_label.setPixmap(self.img.toqpixmap())


app = QApplication(sys.argv)
ex = GitNYellowCircles()
ex.show()
sys.exit(app.exec_())
