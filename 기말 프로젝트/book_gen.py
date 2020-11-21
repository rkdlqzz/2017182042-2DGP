import random
import gfw
import gfw_world
from book import Book

next_gen_small = 0
next_gen_big = 5


def update(t):
    global next_gen_small, next_gen_big
    next_gen_small -= gfw.delta_time
    next_gen_big -= gfw.delta_time
    if next_gen_small < 0:
        gen_small(t)
    if next_gen_big < 0:
        gen_big(t)


def gen_small(t):
    global next_gen_small
    x = random.randint(0, 800)
    speed = -120
    # speed = -(120 + 30 * (t // 10))  # 10초마다 낙하 속도 30씩 증가
    # speed = - 1000
    b = Book(x, speed, 1)
    gfw_world.add(gfw_world.layer.book, b)
    next_gen_small = random.uniform(1, 2)


def gen_big(t):
    global next_gen_big
    x = random.randint(0, 800)
    speed = -150
    b = Book(x, speed, 2)
    gfw_world.add(gfw_world.layer.book, b)
    next_gen_big = random.uniform(5, 6)