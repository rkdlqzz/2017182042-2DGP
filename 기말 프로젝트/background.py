from pico2d import *
import gfw
import generator


class Background:
    def __init__(self, s):
        global student
        self.image1 = gfw.image.load("res/kpu_campus.jpg")
        self.image2 = gfw.image.load("res/kpu_campus2.jpg")
        self.font = gfw.font.load('res/HS여름물빛체.ttf', 70)
        student = s

    def draw(self):
        x = get_canvas_width() // 2
        sx = student.x
        dx = x - sx
        if generator.exam == False:
            self.image1.draw(x + dx * 0.2, 375, 1280, 750)
        else:
            self.image2.draw(x + dx * 0.2, 375, 1280, 750)
            self.font.draw(get_canvas_width() // 2 - 240, get_canvas_height() // 2 + 100, 'MIDTERM EXAM', (200, 0, 0))

    def update(self):
        pass