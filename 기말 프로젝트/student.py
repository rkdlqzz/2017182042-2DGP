from pico2d import *
import gobj


class Student:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT): (-6, 0),
        (SDL_KEYDOWN, SDLK_RIGHT): (6, 0),
        (SDL_KEYUP, SDLK_LEFT): (6, 0),
        (SDL_KEYUP, SDLK_RIGHT): (-6, 0),
    }

    def __init__(self):
        self.x = 400
        self.y = 50
        self.dx = 0
        self.dy = 0
        self.fidx = 0   # 가만히
        self.action = 1  # 왼쪽
        self.image = load_image("res/studentA.png")

    def draw(self):
        sx = self.fidx * 57
        sy = self.action * 99
        self.image.clip_draw(sx, sy, 57, 99, self.x, self.y)

    def update(self):
        self.updateAction()
        gobj.move_obj(self)

    def updateDelta(self, ddx, ddy):
        self.dx += ddx
        self.dy += ddy

    def updateAction(self):     # 플레이어 애니메이션
        self.fidx = (self.fidx + 1) % 7
        if self.dx == 0:
            self.fidx = 0
        elif self.dx > 0:
            self.action = 0
        elif self.dx < 0:
            self.action = 1

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Student.KEY_MAP:
            self.updateDelta(*Student.KEY_MAP[pair])