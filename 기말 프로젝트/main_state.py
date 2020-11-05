import gfw
import gfw_world
from pico2d import *
from student import Student
from background import Background
import book_gen


def enter():
    gfw_world.init(['background', 'student', 'book'])
    global background, student
    background = Background()
    gfw_world.add(gfw_world.layer.background, background)
    student = Student()
    gfw_world.add(gfw_world.layer.student, student)


def update():
    gfw_world.update()
    book_gen.update()
    print('bg:', gfw_world.count_at(0), ' student:', gfw_world.count_at(1), ' book:', gfw_world.count_at(2))


def draw():
    gfw_world.draw()


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


