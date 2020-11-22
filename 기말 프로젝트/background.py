from pico2d import *
import gfw_image
import book_gen


class Background:
    def __init__(self, s):
        global student
        self.image1 = gfw_image.load("res/kpu_campus.jpg")
        self.image2 = gfw_image.load("res/kpu_campus2.jpg")
        student = s

    def draw(self):
        x = get_canvas_width() // 2
        sx = student.x
        dx = x - sx
        if book_gen.exam == False:
            self.image1.draw(x + dx * 0.2, 375, 1280, 750)
        else:
            self.image2.draw(x + dx * 0.2, 375, 1280, 750)

    def update(self):
        pass