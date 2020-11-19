import gfw
import gfw_world
import gfw_font
import gobj
import time
from pico2d import *
from student import Student
from background import Background
import book_gen


def enter():
    gfw_world.init(['background', 'student', 'book'])
    global background, student, start_time
    background = Background()
    gfw_world.add(gfw_world.layer.background, background)
    student = Student()
    gfw_world.add(gfw_world.layer.student, student)
    start_time = time.time()
    global font
    font = gfw_font.load('res/SDMiSaeng.ttf', 50)


def update():
    gfw_world.update()
    book_gen.update(playtime())
    # print('bg:', gfw_world.count_at(0), ' student:', gfw_world.count_at(1), ' book:', gfw_world.count_at(2))
    for b in gfw_world.objects_at(gfw_world.layer.book):
        check_book(b)


def playtime():     # main_state 가 실행된 총 시간을 반환
    now = time.time()
    play_time = now - start_time
    return play_time


def check_book(b):
    if gobj.collides_box(student, b):
        print('collide')
        b.remove()
        return


def draw():
    gfw_world.draw()
    font.draw(20, get_canvas_height() - 40, 'Play time : %d' % book_gen.p_time)
    gobj.draw_collision_box()


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