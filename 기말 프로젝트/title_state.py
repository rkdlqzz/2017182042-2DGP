from pico2d import *
import gfw
import main_state


def enter():
    global bg, panel, font, font2, bg_music
    bg = gfw.image.load('res/gray.png')
    panel = gfw.image.load('res/panel2.png')
    font = gfw.font.load('res/HS여름물빛체.ttf', 50)
    font2 = gfw.font.load('res/HS여름물빛체.ttf', 120)
    bg_music = load_music('res/tbg.mp3')
    bg_music.set_volume(110)
    bg_music.repeat_play()
    global help_, font_h, font_h2, left, right
    help_ = False
    font_h = gfw.font.load('res/godoMaum.ttf', 50)
    font_h2 = gfw.font.load('res/godoMaum.ttf', 80)
    left = gfw.image.load(('res/left.png'))
    right = gfw.image.load(('res/right.png'))
    global character, book1, book2, adrenaline, potion, life
    character = gfw.image.load("res/studentA.png")
    book1 = gfw.image.load('res/book1.png')
    book2 = gfw.image.load('res/book2.png')
    adrenaline = gfw.image.load('res/adrenaline.png')
    potion = gfw.image.load('res/potion.png')
    life = gfw.image.load('res/life.png')


def update():
    pass


def draw():
    w = get_canvas_width()
    h = get_canvas_height()
    bg.draw(w // 2, h // 2, w, h)
    font.draw(130, 120, 'PRESS "SPACE" TO START')
    font.draw(190, 60, 'PRESS "H" TO HELP')
    panel.draw(w // 2, h // 2, w, 800)
    font2.draw(150, 440, 'CAMPUS')
    font2.draw(150, 330, 'LIFE')
    if help_ is True:
        bg.draw(w // 2, h // 2, w, h)
        font_h2.draw(80, 690, '조작법')
        left.draw(120, 600, 60, 60)
        font_h.draw(170, 602, ': 왼쪽으로 이동')
        right.draw(120, 500, 60, 60)
        font_h.draw(170, 502, ': 오른쪽으로 이동')
        font.draw(110, 400, 'P')
        font_h.draw(170, 402, ': 일시정지')
        font_h2.draw(500, 690, '캐릭터')
        character.clip_draw(0, 99, character.w // 7, character.h // 2, 570, 590)
        font_h2.draw(550, 490, '적')
        book1.clip_draw(0, 0, book1.w // 2, book1.h // 4, 500, 390, 70, 70)
        book2.clip_draw(0, 0, book2.w // 2, book2.h // 4, 650, 390, 100, 100)
        font_h.draw(550, 315, '*충돌 시 거대화*')
        font_h2.draw(80, 320, '아이템')
        adrenaline.draw(150, 230, 90, 90)
        font_h.draw(75, 150, '아드레날린')
        font_h.draw(30, 100, '-무적')
        font_h.draw(30, 50, '-충돌 시 보너스 점수')
        potion.draw(420, 230, 90, 90)
        font_h.draw(345, 150, '투명화 포션')
        font_h.draw(310, 100, '-투명화(무적)')
        font_h.draw(310, 50, '-아이템도 못 먹음')
        life.draw(660, 230, 90, 90)
        font_h.draw(635, 150, '목숨')
        font_h.draw(560, 100, '-목숨 +1')
        font_h.draw(560, 50, '-MAX이면 보너스')


def handle_event(e):
    global help_
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.quit()
        elif e.key == SDLK_SPACE:
            gfw.push(main_state)
        elif e.key == SDLK_h:
            if help_ is False:
                help_ = True
            elif help_ is True:
                help_ = False


def exit():
    global bg, panel, font, font2, bg_music
    bg_music.stop()
    del bg, panel, font, font2, bg_music


def pause():
    pass


def resume():
    bg_music.set_volume(110)
    bg_music.repeat_play()


if __name__ == '__main__':
    gfw.run_main()