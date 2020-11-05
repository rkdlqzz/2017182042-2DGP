
objects = []


def init(layer_names):
    global objects, layer
    objects = []
    layer = lambda: None
    layerIndex = 0
    for name in layer_names:
        objects.append([])
        layer.__dict__[name] = layerIndex
        layerIndex += 1


def add(layer_index, obj):
    objects[layer_index].append(obj)


def all_objects():
    for layer_objects in objects:
        for obj in layer_objects:
            yield obj


def objects_at(layer_index):
    for obj in objects[layer_index]:
        yield obj


def count_at(layer_index):
    return len(objects[layer_index])


def clear():
    global objects
    for o in all_objects():
        del o
    objects = []


def clear_at(layer_index):
    for o in objects[layer_index]:
        del o
    objects[layer_index] = []


def update():
    for obj in all_objects():
        obj.update()


def draw():
    for obj in all_objects():
        obj.draw()