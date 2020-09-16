from pico2d import*

open_canvas()

grass = load_image('../res/grass.png')
character = load_image('../res/animation_sheet.png')
frame_index = 0
action = 0
for x in range(0, 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100*frame_index, 100*action, 100, 100, x, 80)
    update_canvas()

    get_events()

    frame_index = (frame_index+1) % 8
    if (x % 100) == 0:
        action = (action+1) % 4

    delay(0.0001)


close_canvas()
