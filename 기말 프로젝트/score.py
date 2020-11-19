import gfw_image
import main_state

class Score:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()

    def reset(self):
        self.score = 0
        self.display = 0

    def draw(self):
        main_state.score_font.draw(self.x, self.y, '%d' % self.display)

    def update(self):
    	if self.display < self.score:
            self.display += 1