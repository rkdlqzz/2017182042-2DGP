import gfw
import gobj
import time
from pico2d import *
from student import Student
from background import Background
from score import Score
import generator

paused = False


def enter():
    gfw.world.init(['background', 'book', 'student', 'ui'])
    global student
    student = Student()
    gfw.world.add(gfw.world.layer.student, student)
    global background
    background = Background(student)
    gfw.world.add(gfw.world.layer.background, background)
    global start_time
    start_time = time.time()
    global font
    font = gfw.font.load('res/HS여름물빛체.ttf', 40)
    global score
    score = Score(30, get_canvas_height() - 50)
    gfw.world.add(gfw.world.layer.ui, score)
    global paused_time
    paused_time = 0


def update():
    global paused_time
    if paused:
        paused_time += gfw.delta_time
        return
    gfw.world.update()
    generator.update(playtime())
    # print('bg:', gfw.world.count_at(0), ' student:', gfw.world.count_at(1), ' book:', gfw.world.count_at(2))
    for b in gfw.world.objects_at(gfw.world.layer.book):
        check_book(b)
    score.score += gfw.delta_time
    exam_time(generator.exam)


def playtime():     # main_state 가 실행된 총 시간 - pause 된 시간
    now = time.time()
    play_time = now - start_time - paused_time
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


def exam_time(exam):    # 시험기간에는 애니메이션 속도 증가 & book 크기 증가
    if exam:
        for b in gfw.world.objects_at(gfw.world.layer.book):
            b.time += gfw.delta_time
            if b.size == 70 or b.size == 100:
                b.size += 20
    else:
        for b in gfw.world.objects_at(gfw.world.layer.book):
            if b.size != 70 and b.size != 100:
                b.size -= 20


def draw():
    gfw.world.draw()
    font.draw(get_canvas_width() - 250, get_canvas_height() - 35, 'STAGE - %d학년' % (generator.stage + 1))
    font.draw(get_canvas_width() - 550, get_canvas_height() - 40, 'time %d' % (playtime() + 1))
    if paused:
        pause()
    # gobj.draw_collision_box()


def pause():
    x = get_canvas_width() // 2 - 25
    y = get_canvas_height() // 2 - 30
    fy = y - 2
    panel = gfw.image.load('res/panel.png')
    panel.draw(x, y, get_canvas_width(), get_canvas_height() - 50)
    bg = gfw.image.load('res/gray.png')
    for n in [150, 0, -150]:
        bg.draw(x + 25, y + n, 360, 60)
    font.draw(x - 145, fy + 150, 'PRESS P TO RESUME')
    font.draw(x - 145, fy, 'PRESS ESC TO TITLE')
    font.draw(x - 115, fy - 150, 'CLICK X TO QUIT')


def handle_event(e):
    global student
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_p:
            global paused
            paused = not paused

    student.handle_event(e)


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()