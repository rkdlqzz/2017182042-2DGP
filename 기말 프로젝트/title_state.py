import gfw
from pico2d import *
import main_state


def enter():
    global title, press, tbg
    title = load_image('res/title.png')
    press = load_image('res/press.png')
    tbg = load_image('res/tbg.png')


def update():
    pass


def draw():
    tbg.draw(400, 375, 800, 750)
    press.draw(400, 120)
    title.draw(395, 450)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)


def exit():
    global title, press, tbg
    del title, press, tbg


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
