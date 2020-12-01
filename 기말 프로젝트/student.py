from pico2d import *
import gfw
import gobj


class Student:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT): (-1.5, 0),
        (SDL_KEYDOWN, SDLK_RIGHT): (1.5, 0),
        (SDL_KEYUP, SDLK_LEFT): (1.5, 0),
        (SDL_KEYUP, SDLK_RIGHT): (-1.5, 0),
    }

    def __init__(self):
        self.x = get_canvas_width() / 2
        self.y = 50
        self.dx = 0
        self.dy = 0
        self.fidx = 0   # 가만히
        self.action = 1  # 왼쪽
        self.time = 0
        self.life = 3
        self.image1 = gfw.image.load("res/studentA.png")
        self.image2 = gfw.image.load("res/studentA_invisible.png")
        self.image = self.image1
        self.life_image = gfw.image.load("res/life.png")
        self.s_width = self.image.w // 7
        self.s_height = self.image.h // 2
        self.minx = self.s_width / 2
        self.maxx = get_canvas_width() - self.s_width / 2
        self.size_w = 57    # 77
        self.size_h = 99    # 119
        self.scale_time = 0
        self.invisible_time = 0
        self.status_invisible = False

    def draw(self):
        # print(self.s_width, self.s_height)
        sx = self.fidx * self.s_width
        sy = self.action * self.s_height
        self.image.clip_draw(sx, sy, self.s_width, self.s_height, self.x, self.y, self.size_w, self.size_h)
        n = self.life
        while n > 0:
            self.life_image.draw(650 + (3 - n) * 55, 665, 60, 60)
            n -= 1

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
        self.update_size()
        self.update_image()

    def updateDelta(self, ddx, ddy):
        self.dx += ddx
        self.dy += ddy

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Student.KEY_MAP:
            self.updateDelta(*Student.KEY_MAP[pair])

    def get_bb(self):
        halfw = self.size_w // 2 - 12
        halfh = self.size_h // 2
        return self.x - halfw, self.y - halfh + 15, self.x + halfw, self.y + halfh

    def decrease_life(self):
        self.life -= 1
        return self.life <= 0

    def update_size(self):  # book2와 충돌 시 student 잠시 거대화
        s_max = 25  # 최대 증가량
        if self.scale_time > 0:
            self.scale_time -= gfw.delta_time
        else:
            self.scale_time = 0
        if (self.scale_time > 0 and self.size_w < 57 + s_max):
            self.size_w += 1
            self.size_h += 1.1
        if (self.scale_time == 0 and self.size_w > 57):
            self.size_w -= 1
            self.size_h -= 1.1

    def update_image(self):  # 투명화 체크
        if self.invisible_time > 0:
            self.invisible_time -= gfw.delta_time
            if self.invisible_time < 1.3:   # 투명화 지속시간이 얼마 안남으면 깜빡거림
                if self.image == self.image1:
                    self.image = self.image2
                elif self.image == self.image2:
                    self.image = self.image1
        else:
            self.invisible_time = 0
            self.image = self.image1
            self.status_invisible = False