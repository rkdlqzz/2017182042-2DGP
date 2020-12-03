from pico2d import *
import gfw


class Item:
    def __init__(self, x, type, speed):
        self.type = type
        if self.type == 1:
            self.image = gfw.image.load('res/potion.png')
        if self.type == 2:
            self.image = gfw.image.load('res/life.png')
        if self.type == 3:
            self.image = gfw.image.load('res/adrenaline.png')
        self.size = 70
        self.x, self.y = x, get_canvas_height() + self.size
        self.dx, self.dy = 0, speed
        self.time = 0

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        self.time += gfw.delta_time
        self.y += self.dy * gfw.delta_time

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        if self.type == 1:
            halfw = self.size // 2 - 15
            halfh = self.size // 2
        elif self.type == 2:
            halfw = self.size // 2 - 10
            halfh = self.size // 2 - 12
        elif self.type == 3:
            halfw = self.size // 2 - 20
            halfh = self.size // 2
        return self.x - halfw, self.y - halfh, self.x + halfw, self.y + halfh