from pico2d import*

open_canvas()
character = load_image("../res/character.png")
grass = load_image("../res/grass.png")

for x in range(0, 801, 100):
    for y in range(0, 801, 100):
        delay(0.03)
        character.draw_now(x, y)
        delay(0.03)
        grass.draw_now(x-50, y-50)

close_canvas()

