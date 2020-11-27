from pico2d import *
import gfw

def point_add(posx, posy, deltax, deltay):
    x1 = posx + deltax
    y1 = posy + deltay
    return x1, y1


def move_obj(obj):
    obj.x, obj.y = point_add(obj.x, obj.y, obj.dx, obj.dy)


def collides_box(a, b):
    (la, ba, ra, ta) = a.get_bb()
    (lb, bb, rb, tb) = b.get_bb()

    if la > rb:
        return False
    if ra < lb:
        return False
    if ba > tb:
        return False
    if ta < bb:
        return False

    return True


def draw_collision_box():
    for obj in gfw.world.all_objects():
        if hasattr(obj, 'get_bb'):
            draw_rectangle(*obj.get_bb())