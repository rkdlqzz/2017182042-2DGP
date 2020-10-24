from pico2d import *
import gfw_image


class Background:
    def __init__(self):
        self.image = gfw_image.load("res/kpu_campus.jpg")

    def draw(self):
        self.image.draw(400, 400, 1000, 800)

    def update(self):
        pass