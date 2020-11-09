import random
import gfw
import gfw_world
from book import Book

next_wave = 0
b_index = 0


def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()


def generate_wave():
    global b_index, next_wave
    x = random.randint(0, 800)
    speed = -(120 + 10 * b_index)
    b = Book(x, speed)
    gfw_world.add(gfw_world.layer.book, b)
    b_index += 1
    next_wave = random.uniform(1, 2)

