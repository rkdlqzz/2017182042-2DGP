import gfw
from pico2d import *
from student import Student
from background import Background


def enter():
    global background, student
    background = Background()
    student = Student()


def update():
    student.update()


def draw():
    background.draw()
    student.draw()


def handle_event(e):
    global student
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    student.handle_event(e)


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()


