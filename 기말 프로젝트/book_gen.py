import random
import gfw
import gfw_world
import main_state
from book import Book

next_wave = 0
p_time = 0

def update():
    global next_wave, p_time
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()
    print(main_state.playtime())
    p_time = main_state.playtime()


def generate_wave():
    global b_index, next_wave
    x = random.randint(0, 800)

    speed = -(120 + 30 * (main_state.playtime() // 10))     # 10초마다 낙하 속도 30씩 증가
    b = Book(x, speed)
    gfw_world.add(gfw_world.layer.book, b)

    next_wave = random.uniform(1, 2)