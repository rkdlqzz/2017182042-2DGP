import gfw_image


class Background:
    def __init__(self):
        self.image = gfw_image.load("res/kpu_campus.jpg")

    def draw(self):
        self.image.draw(400, 375, 1280, 750)

    def update(self):
        pass