

def point_add(posx, posy, deltax, deltay):

    x1 = posx + deltax
    y1 = posy + deltay
    return x1, y1


def move_obj(obj):
    obj.x, obj.y = point_add(obj.x, obj.y, obj.dx, obj.dy)