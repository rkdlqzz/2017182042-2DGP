import gfw
from pico2d import *
import main_state


def enter():
    global image, elapsed
    image = load_image('res/kpu_logo.png')
    elapsed = 0


def update():
    global elapsed
    elapsed += gfw.delta_time
    if elapsed > 1.0:
        gfw.change(main_state)


def draw():
    image.draw(400, 375, 800, 750)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()


def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
