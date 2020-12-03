import gfw
import gobj
import time
from pico2d import *
from student import Student
from background import Background
from score import Score
import generator
import highscore

paused = False
IN_GAME, GAME_OVER = 0, 1
state = IN_GAME
black_w = 370


def enter():
    global state
    state = IN_GAME
    gfw.world.init(['background', 'student', 'item', 'book', 'highscore', 'ui'])
    global student
    student = Student()
    gfw.world.add(gfw.world.layer.student, student)
    global background
    background = Background(student)
    gfw.world.add(gfw.world.layer.background, background)
    global start_time
    start_time = time.time()
    global font, font2
    font = gfw.font.load('res/HS여름물빛체.ttf', 40)
    font2 = gfw.font.load('res/HS여름물빛체.ttf', 55)
    global score
    score = Score(30, get_canvas_height() - 50)
    gfw.world.add(gfw.world.layer.ui, score)
    global paused_time, paused
    paused_time = 0
    paused = False
    highscore.load()
    global rectangle, black, panel, gray
    rectangle = gfw.image.load('res/rectangle.png')
    black = gfw.image.load('res/black.png')
    panel = gfw.image.load('res/panel.png')
    gray = gfw.image.load('res/gray.png')
    generator.last_stage = -1
    global bg_music1, bg_music2, play_music1, play_music2, collide_b_wav
    bg_music1 = load_music('res/bg1.mp3')
    bg_music1.set_volume(50)
    bg_music1.repeat_play()
    play_music1 = True
    bg_music2 = load_music('res/bg2.mp3')
    play_music2 = False
    collide_b_wav = load_wav('res/c_b.wav')
    global bonus_wav, collide_i_wav, game_over_wav, button_wav
    bonus_wav = load_wav('res/bonus.wav')
    collide_i_wav = load_wav('res/c_i.wav')
    game_over_wav = load_wav('res/gameover.wav')
    button_wav = load_wav('res/button.wav')


def update():
    global state
    if state == GAME_OVER:
        return
    if paused:
        paused_update()
        return
    gfw.world.update()
    generator.update(playtime())
    for b in gfw.world.objects_at(gfw.world.layer.book):
        check_book(b)
    for i in gfw.world.objects_at(gfw.world.layer.item):
        check_item(i)
    score.score += gfw.delta_time
    exam_time(generator.exam)
    update_music()


def paused_update():    # pause 시 update 해줄 것 - book 애니메이션
    global paused_time
    paused_time += gfw.delta_time
    for b in gfw.world.objects_at(gfw.world.layer.book):
        b.time += gfw.delta_time
        b.fidx = int(b.time * 12) % 8


def check_book(b):
    if gobj.collides_box(student, b):
        if student.status_invisible is True:    # 투명상태이면 충돌해도 변화 x
            return
        if student.status_angry is True:    # angry 상태이면 충돌시 더 많은 점수 획득 & 무적
            bonus_wav.play()
            score.score += 10
            b.remove()
            return
        if student.decrease_life():
            game_over_wav.play()
            end_game()
        collide_b_wav.play()
        if b.type == 2:  # book2와 충돌 시 student 거대화
            student.scale_time = 5
        score.score += 5
        b.remove()
        return
    if b.y < -b.size + 50:
        b.remove()
        score.score += 5


def check_item(i):  # item과 충돌
    if gobj.collides_box(student, i):
        if student.status_invisible is True:    # 투명화 상태에서는 다른 item 먹을 수 없음
            return
        if i.type == 1:     # 투명화
            collide_i_wav.play()
            student.invisible_time = 5
            student.status_invisible = True
            student.image = student.image2
            if student.status_angry is True:    # angry 상태에서 투명화되면 angry 효과 해제
                student.status_angry = False
                student.angry_time = 0
                student.fire = None
        if i.type == 2:     # 라이프
            if student.increase_life():  # life가 max인 경우 추가점수
                bonus_wav.play()
                score.score += 30
            else:
                collide_i_wav.play()
        if i.type == 3:     # 아드레날린 주사
            collide_i_wav.play()
            student.status_angry = True
            student.angry_time = 5
            student.fire = student.fire_image
        i.remove()
        return
    if i.y < -i.size + 50:
        i.remove()


def playtime():     # main_state 가 실행된 총 시간 - pause 된 시간
    now = time.time()
    play_time = now - start_time - paused_time
    return play_time


def exam_time(exam):    # 시험기간에는 애니메이션 속도 증가 & book 크기 증가
    ds = 1  # update 당 size 증가량
    s_max = 25  # 최대 증가량
    if exam:
        for b in gfw.world.objects_at(gfw.world.layer.book):
            b.time += gfw.delta_time
            if b.type == 1 and b.size < 70 + s_max:
                b.size += ds
            elif b.type == 2 and b.size < 100 + s_max:
                b.size += ds
    else:
        for b in gfw.world.objects_at(gfw.world.layer.book):
            if b.type == 1 and b.size > 70:
                b.size -= ds
            elif b.type == 2 and b.size > 100:
                b.size -= ds


def update_music():     # 기본, exam_time 배경음악 변경
    global bg_music1, bg_music2, play_music1, play_music2
    for i in range(0, 30):
        if int(playtime()) == (i * generator.stage_cycle) - generator.exam_cycle:
            if play_music1 is True:
                bg_music1.stop()
                play_music1 = False
            if play_music2 is False:
                bg_music2.repeat_play()
                play_music2 = True
        if int(playtime()) == (i * generator.stage_cycle):
            if play_music2 is True:
                bg_music2.stop()
                play_music2 = False
            if play_music1 is False:
                bg_music1.repeat_play()
                play_music1 = True
    if play_music2 is True:
        bg_music1.set_volume(130)
    else:
        bg_music1.set_volume(50)


def draw():
    gfw.world.draw()
    font.draw(get_canvas_width() - 250, get_canvas_height() - 35, 'STAGE - %d학년' % (generator.stage + 1))
    display_stage()
    if paused:
        paused_draw()
    if state == GAME_OVER:
        highscore.draw()
    # gobj.draw_collision_box()


def paused_draw():  # pause 시 메뉴 그리기
    x = get_canvas_width() // 2 - 25
    y = get_canvas_height() // 2 - 30
    fy = y - 2
    panel.draw(x, y, get_canvas_width(), get_canvas_height() - 50)
    gray.draw(400, 623, 250, 60)
    font2.draw(330, 620, 'MENU')
    for n in [150, 0, -150]:
        gray.draw(x + 25, y + n, 360, 60)
    font.draw(x - 145, fy + 150, 'PRESS P TO RESUME')
    font.draw(x - 145, fy, 'PRESS ESC TO TITLE')
    font.draw(x - 115, fy - 150, 'CLICK X TO QUIT')


def display_stage():    # stage 변경 시
    global black_w
    if generator.display_time != 0:
        if generator.display_time <= 3:
            black.draw(get_canvas_width() // 2, 470, black_w, 170)
            if generator.display_time == 3:
                pass
            if black_w <= 1100:
                black_w += 10
            rectangle.draw(get_canvas_width() // 2, get_canvas_height() // 2 + 100, 400, 110)
            font.draw(get_canvas_width() // 2 - 60, get_canvas_height() // 2 + 100, 'STAGE %d'\
                      % (generator.stage + 1), (200, 200, 200))
        if not paused and not state == GAME_OVER:
            generator.display_time -= gfw.delta_time
    if generator.display_time < 0:
        black_w = 370
        generator.display_time = 0


def start_game():
    global state, score
    if state != GAME_OVER:
        return
    score.reset()
    gfw.world.remove(highscore)
    state = IN_GAME
    enter()
    generator.last_stage = -2
    global black_w
    black_w = 370


def end_game():
    global state
    if state != IN_GAME:
        return
    state = GAME_OVER
    highscore.add(score.score)
    gfw.world.add(gfw.world.layer.highscore, highscore)


def handle_event(e):
    global student
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            end_game()
            gfw.pop()
        elif e.key == SDLK_p:
            button_wav.play()
            global paused
            if state != GAME_OVER:
                paused = not paused
        elif e.key == SDLK_RETURN:
            start_game()
        elif e.key == SDLK_e:
            if not paused:
                end_game()

    student.handle_event(e)


def exit():
    global bg_music1, bg_music2, collide_b_wav, collide_i_wav, bonus_wav, game_over_wav
    bg_music1.stop()
    bg_music2.stop()
    del bg_music1, bg_music2, collide_b_wav, collide_i_wav, bonus_wav, game_over_wav


if __name__ == '__main__':
    gfw.run_main()