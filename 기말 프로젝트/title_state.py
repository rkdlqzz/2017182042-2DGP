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