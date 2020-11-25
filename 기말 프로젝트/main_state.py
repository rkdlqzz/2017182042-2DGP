import gfw
import gfw_world
import gfw_font
import gobj
import time
from pico2d import *
from student import Student
from background import Background
from score import Score
import generator


def enter():
    gfw_world.init(['background', 'book', 'student', 'ui'])
    global student
    student = Student()
    gfw_world.add(gfw_world.layer.student, student)
    global background
    background = Background(student)
    gfw_world.add(gfw_world.layer.background, background)
    global start_time
    start_time = time.time()
    global font
    font = gfw_font.load('res/HS여름물빛체.ttf', 40)
    global score
    score = Score(30, get_canvas_height() - 50)
    gfw_world.add(gfw_world.layer.ui, score)


def update():
    gfw_world.update()
    generator.update(playtime())
    # print('bg:', gfw_world.count_at(0), ' student:', gfw_world.count_at(1), ' book:', gfw_world.count_at(2))
    for b in gfw_world.objects_at(gfw_world.layer.book):
        check_book(b)
    score.score += gfw.delta_time


def playtime():     # main_state 가 실행된 총 시간을 반환
    now = time.time()
    play_time = now - start_time
    return play_time


def check_book(b):
    if gobj.collides_box(student, b):
        # student.decrease_life()
        if student.life == 0:
            gfw.quit()
        score.score += 5
        b.remove()
        return
    if b.y < -b.SIZE:
        b.remove()
        score.score += 5


def draw():
    gfw_world.draw()
    font.draw(get_canvas_width() - 250, get_canvas_height() - 35, 'STAGE - %d학년' % (generator.stage + 1))
    font.draw(get_canvas_width() - 550, get_canvas_height() - 40, 'time %d' % playtime())
    # gobj.draw_collision_box()



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