import random
import gfw
import gfw_world
from book import Book

next_wave = 0


def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()


def generate_wave():
    global wave_index, next_wave
    x=random.randint(0, 800)
    speed = -120
    b = Book(x, speed)
    gfw_world.add(gfw_world.layer.book, b)

    next_wave = random.uniform(1, 2)

