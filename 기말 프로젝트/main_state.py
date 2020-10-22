from pico2d import *
from student import Student
from background import Background


def handle_events(e):
    global running
    if e.type == SDL_QUIT:
        running = False
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        running = False
    student.handle_event(e)


open_canvas(800,750)

background = Background()
student = Student()

running = True
while running:
    clear_canvas()
    background.draw()
    student.draw()

    update_canvas()

    evts = get_events()
    for e in evts:
        handle_events(e)

    student.update()
    background.update()

    delay(0.05)

close_canvas()


