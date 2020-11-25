from pico2d import *
import random
import gfw
import gfw_world
from book import Book

next_gen_small = 0
next_gen_big = 5


def update(t):
    global next_gen_small, next_gen_big, stage, stage_cycle,exam, exam_cycle
    # stage_cycle = 60    # stage 나누는 주기
    stage_cycle = 6
    stage = t // stage_cycle
    if stage > 3:   # stage 최대 4
        stage = 3
    # exam_cycle = 15   # 시험기간 몇 초인지
    exam_cycle = 3
    exam = check_exam(t)
    next_gen_small -= gfw.delta_time
    next_gen_big -= gfw.delta_time
    if next_gen_small < 0:
        gen_small()
    if next_gen_big < 0:
        gen_big()


def gen_small():
    global next_gen_small
    for x in range(1, int(stage) + 2):  # stage 당 생성되는 book 개수 : 1, 2, 3, 4
        x = random.randint(0, 800)
        sy = random.randint(0, 150)  # y값 = 캔버스 맨위 + sy (한번에 여러개의 book이 생성되어도 y위치가 다르게)
        speed = -110 - (30 * stage) - random.randint(0, 20)  # stage 따라서 속도 증가, 같은 stage라도 랜덤하게(+-10)
        b = Book(x, speed, 1, stage * sy)
        gfw_world.add(gfw_world.layer.book, b)
    next = 1 - stage * 0.1  # 초기 - 1~2초마다 젠, stage 증가할수록 젠시간 감소
    next_gen_small = random.uniform(next, next + 1)


def gen_big():
    global next_gen_big
    x = random.randint(0, 800)
    speed = -150 - (30 * stage)
    b = Book(x, speed, 2, 0)
    gfw_world.add(gfw_world.layer.book, b)
    next = 5 - stage * 1.2   # 초기 - 5~6초마다 젠, stage 증가할수록 젠시간 감소
    next_gen_big = random.uniform(next, next + 1)


def check_exam(t):  # 시험기간인지 체크
    global stage
    if (t - stage * stage_cycle) >= (stage_cycle - exam_cycle) and (t - stage * stage_cycle) <= stage_cycle :
        return True
    else:
        return False
