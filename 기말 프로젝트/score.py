import gfw


class Score:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()
        self.font = gfw.font.load('res/HS여름물빛체.ttf', 70)

    def reset(self):
        self.score = 0
        self.display = 0

    def draw(self):
        self.font.draw(self.x, self.y, '%d' % self.display)

    def update(self):
    	if self.display < self.score:
            self.display += 1