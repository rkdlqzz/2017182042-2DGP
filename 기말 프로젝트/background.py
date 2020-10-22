from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image("res/kpu_campus.jpg")

    def draw(self):
        self.image.draw(400, 400, 1000, 800)

    def update(self):
        pass