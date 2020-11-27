from pico2d import *
import gfw
import main_state


def enter():
    global bg, panel, font, font2
    bg = gfw.image.load('res/gray.png')
    panel = gfw.image.load('res/panel2.png')
    font = gfw.font.load('res/HS여름물빛체.ttf', 50)
    font2 = gfw.font.load('res/HS여름물빛체.ttf', 120)


def update():
    pass


def draw():
    w = get_canvas_width()
    h = get_canvas_height()
    bg.draw(w // 2, h // 2, w, h)
    font.draw(150, 90, 'PRESS SPACE TO START')
    panel.draw(w // 2, h // 2, w, 800)
    font2.draw(150, 440, 'CAMPUS')
    font2.draw(150, 330, 'LIFE')


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)


def exit():
    global bg, panel, font, font2
    del bg, panel, font, font2


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()