from pico2d import *
import random
import gfw
from book import Book
from item import Item

next_gen_small = 0
next_gen_big = 5
next_gen_item = 5
last_stage = -1
display_time = 0


def update(t):
    global next_gen_small, next_gen_big, stage, stage_cycle, exam, exam_cycle, last_stage, display_time, next_gen_item
    stage_cycle = 45    # stage 나누는 주기
    # stage_cycle = 10  # 디버깅 용
    # stage = 3   # 디벙깅 용
    stage = t // stage_cycle
    if stage > 3:   # stage 최대 4
        stage = 3
    if stage > last_stage:  # stage가 바뀌는 경우
        display_time = 4
        last_stage += 1
    exam_cycle = 15   # 시험기간 몇 초인지
    # exam_cycle = 5    # 디버깅 용
    exam = check_exam(t)
    next_gen_small -= gfw.delta_time
    next_gen_big -= gfw.delta_time
    next_gen_item -= gfw.delta_time
    if next_gen_small < 0:
        gen_small()
    if next_gen_big < 0:
        gen_big()
    if next_gen_item < 0:
        gen_item()


def gen_small():
    global next_gen_small
    for i in range(1, int(stage) + 3):  # stage 당 생성되는 book 개수 : 2, 3, 4, 5
        x = random.randint(0, 800)
        sy = random.randint(0, 150)  # y값 = 캔버스 맨위 + sy (한번에 여러개의 book이 생성되어도 y위치가 다르게)
        speed = -110 - (30 * stage) - random.randint(0, 20)  # stage 따라서 속도 증가, 같은 stage라도 랜덤하게(+-10)
        b = Book(x, speed, 1, (stage+1) * sy)
        gfw.world.add(gfw.world.layer.book, b)
    next = 1 - stage * 0.1  # 초기 - 1~2초마다 젠, stage 증가할수록 젠시간 감소
    next_gen_small = random.uniform(next, next + 1)


def gen_big():
    global next_gen_big
    for i in range(1, (int(stage) // 2) + 2):  # stage 당 생성되는 book 개수 : 1, 1, 2, 2
        x = random.randint(0, 800)
        sy = random.randint(0, 200)
        speed = -150 - (30 * stage)
        b = Book(x, speed, 2, (stage // 2) * sy)
        gfw.world.add(gfw.world.layer.book, b)
    next = 5 - stage * 1.2   # 초기 - 5~6초마다 젠, stage 증가할수록 젠시간 감소
    next_gen_big = random.uniform(next, next + 1)


def gen_item():
    global next_gen_item
    x = random.randint(0, 800)
    type = random.randint(1, 3)     # item type 랜덤하게
    speed = -100 - (15 * stage)
    i = Item(x, type, speed)
    gfw.world.add(gfw.world.layer.item, i)
    next = 5 - stage  # 초기 - 5~6초마다 젠, stage 증가할수록 젠시간 감소
    next_gen_item = random.uniform(next, next + 1)


def check_exam(t):  # 시험기간인지 체크
    global stage
    for i in range(0, 30):  # stage 4의 경우 stage가 증가하지 않더라도 시험기간은 계속 주기적으로 된다
        if (t - i * stage_cycle) >= (stage_cycle - exam_cycle) and (t - i * stage_cycle) <= stage_cycle:
            return True
    else:
        return False