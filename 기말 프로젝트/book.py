from pico2d import *
import gfw
import gfw_world
import gfw_image


class Book:
    SIZE = 141

    def __init__(self, x, speed):
        self.x, self.y = x, get_canvas_height() + Book.SIZE
        self.dx, self.dy = 0, speed
        self.image = gfw_image.load('res/book1.png')
        self.fidx = 0
        self.b_width = self.image.w // 2
        self.b_height = self.image.h // 4
        self.time = 0

    def draw(self):
        sx = self.b_width - (self.fidx % 2) * self.b_width
        sy = (self.fidx // 2) * self.b_height
        self.image.clip_draw(sx, sy, self.b_width, self.b_height, self.x, self.y, 70, 70)

    def update(self):
        self.time += gfw.delta_time
        self.fidx = int(self.time * 12) % 8
        self.y += self.dy * gfw.delta_time

        if self.y < -Book.SIZE:
            self.remove()

    def remove(self):
        gfw_world.remove(self)
