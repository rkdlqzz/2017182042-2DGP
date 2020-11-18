from pico2d import *
import gfw_image
import gfw
import gobj


class Student:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT): (-1.5, 0),
        (SDL_KEYDOWN, SDLK_RIGHT): (1.5, 0),
        (SDL_KEYUP, SDLK_LEFT): (1.5, 0),
        (SDL_KEYUP, SDLK_RIGHT): (-1.5, 0),
    }
    image = None

    def __init__(self):
        self.x = get_canvas_width() / 2
        self.y = 50
        self.dx = 0
        self.dy = 0
        self.fidx = 0   # 가만히
        self.action = 1  # 왼쪽
        self.time = 0
        if Student.image == None:
            Student.image = gfw_image.load("res/studentA.png")
        self.s_width = self.image.w // 7
        self.s_height = self.image.h // 2
        self.minx = self.s_width / 2
        self.maxx = get_canvas_width() - self.s_width / 2

    def draw(self):
        sx = self.fidx * self.s_width
        sy = self.action * self.s_height
        self.image.clip_draw(sx, sy, self.s_width, self.s_height, self.x, self.y)

    def update(self):
        self.x = clamp(self.minx, self.x, self.maxx)    # 플레이어가 화면을 벗어나지 못하도록
        if self.dx == 0:
            self.fidx = 0
        else:
            self.time += gfw.delta_time
            frame = self.time * 10
            self.fidx = int(frame) % 7
            if self.dx > 0:
                self.action = 0
            elif self.dx < 0:
                self.action = 1
        gobj.move_obj(self)

    def updateDelta(self, ddx, ddy):
        self.dx += ddx
        self.dy += ddy

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Student.KEY_MAP:
            self.updateDelta(*Student.KEY_MAP[pair])

    def get_bb(self):
        halfw = self.s_width // 2 - 10
        halfh = self.s_height // 2
        return self.x - halfw, self.y - halfh, self.x + halfw, self.y + halfh