from pico2d import *
import gfw_image


class Background:
    def __init__(self, s):
        global student
        self.image = gfw_image.load("res/kpu_campus.jpg")
        student = s

    def draw(self):
        x = get_canvas_width() // 2
        sx = student.x
        dx = x - sx
        self.image.draw(x + dx * 0.2, 375, 1280, 750)
        # self.image.draw(400, 375, 1280, 750)

    def update(self):
        pass