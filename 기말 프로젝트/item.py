from pico2d import *
import gfw


class Item:
    def __init__(self, x, type):
        self.type = type
        if self.type == 1:
            self.size = 70
        if self.type == 2:
            self.size = 100
        self.x, self.y = x, get_canvas_height() + self.size
        self.dx, self.dy = 0, -100
        self.image = gfw.image.load('res/potion.png')
        self.time = 0

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        self.time += gfw.delta_time
        self.y += self.dy * gfw.delta_time

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        halfw = self.size // 2 - 15
        halfh = self.size // 2
        return self.x - halfw, self.y - halfh, self.x + halfw, self.y + halfh