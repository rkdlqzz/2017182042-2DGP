import gfw
import gfw_world
import time
from pico2d import *
from student import Student
from background import Background
import book_gen


def enter():
    global start_time
    gfw_world.init(['background', 'student', 'book'])
    global background, student, start_time
    background = Background()
    gfw_world.add(gfw_world.layer.background, background)
    student = Student()
    gfw_world.add(gfw_world.layer.student, student)
    start_time = time.time()


def update():
    gfw_world.update()
    book_gen.update()

    
def playtime():     # main_state 가 실행된 총 시간을 반환
    now = time.time()
    play_time = now - start_time
    return play_time


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
