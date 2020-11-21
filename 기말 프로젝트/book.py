from pico2d import *
import gfw
import gfw_world
import gfw_image


class Book:
    SIZE = 141

    def __init__(self, x, speed, type, sy):
        self.x, self.y = x, get_canvas_height() + Book.SIZE + sy
        self.dx, self.dy = 0, speed
        self.type = type
        self.image = gfw_image.load('res/book%d.png' % type)
        self.fidx = 0
        self.b_width = self.image.w // 2
        self.b_height = self.image.h // 4
        self.time = 0
        if self.type == 1:
            self.size = 70
            self.s = 7
        if self.type == 2:
            self.size = 100
            self.s = 15

    def draw(self):
        sx = self.b_width - (self.fidx % 2) * self.b_width
        sy = (self.fidx // 2) * self.b_height
        self.image.clip_draw(sx, sy, self.b_width, self.b_height, self.x, self.y, self.size, self.size)

    def update(self):
        self.time += gfw.delta_time
        self.fidx = int(self.time * 12) % 8
        self.y += self.dy * gfw.delta_time

    def remove(self):
        gfw_world.remove(self)

    def get_bb(self):
        halfw = self.size // 2
        halfh = self.size // 2 - self.s
        return self.x - halfw + self.s, self.y - halfh, self.x + halfw, self.y + halfh