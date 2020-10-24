from pico2d import *
import gfw_image
import gobj


class Student:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT): (-6, 0),
        (SDL_KEYDOWN, SDLK_RIGHT): (6, 0),
        (SDL_KEYUP, SDLK_LEFT): (6, 0),
        (SDL_KEYUP, SDLK_RIGHT): (-6, 0),
    }
    image = None

    def __init__(self):
        self.x = 400
        self.y = 50
        self.dx = 0
        self.dy = 0
        self.fidx = 0   # 가만히
        self.action = 1  # 왼쪽
        self.minx = 57 / 2
        self.maxx = get_canvas_width() - 57 / 2
        if Student.image == None:
            Student.image = gfw_image.load("res/studentA.png")

    def draw(self):
        sx = self.fidx * 57
        sy = self.action * 99
        self.image.clip_draw(sx, sy, 57, 99, self.x, self.y)

    def update(self):
        self.x = clamp(self.minx, self.x, self.maxx)    # 플레이어가 화면을 벗어나지 못하도록
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