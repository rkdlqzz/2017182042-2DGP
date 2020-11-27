from pico2d import *
import pickle
import time
import gfw

FILENAME = 'data.pickle'
scores = []
MAX_SCORE_COUNT = 10
last_rank = -1

class Entry:
    def __init__(self, score):
        self.score = score
        self.time = time.time()

def load():
    global font, font2, panel, bg
    font = gfw.font.load(('res/HS여름물빛체.ttf'), 20)
    font2 = gfw.font.load(('res/HS여름물빛체.ttf'), 50)
    panel = gfw.image.load('res/panel.png')
    bg = gfw.image.load('res/gray.png')

    global scores
    try:
        f = open(FILENAME, "rb")
        scores = pickle.load(f)
        f.close()
        #print("Scores:", scores)
    except:
        print("No highscore file")

def save():
    f = open(FILENAME, "wb")
    pickle.dump(scores, f)
    f.close()

def add(score):
    global scores, last_rank
    entry = Entry(score)
    inserted = False
    for i in range(len(scores)):
        e = scores[i]
        if e.score < entry.score:
            scores.insert(i, entry)
            inserted = True
            last_rank = i + 1
            break
    if not inserted:
        scores.append(entry)
        last_rank = len(scores)

    if (len(scores) > MAX_SCORE_COUNT):
        scores.pop(-1)
    if last_rank <= MAX_SCORE_COUNT:
        save()

def draw():
    global font, font2, last_rank, panel, bg
    x = get_canvas_width() // 2 - 25
    y = get_canvas_height() // 2 - 30
    panel.draw(x, y, get_canvas_width(), get_canvas_height() - 50)
    bg.draw(400, 625, 300, 60)
    bg.draw(400, 572, 420, 30)
    font2.draw(275, 620, 'GAME OVER')
    font.draw(200, 570, 'RANK   SCORE                       DATE')
    rank = 1
    y = 530
    color = (0, 0, 0)
    for e in scores:
        bg.draw(400, y + 47 - 45, 420, 30)
        str = "{:2d} {:10d}".format(rank, int(e.score))
        font.draw(210, y, str, color)
        font.draw(360, y, time.asctime(time.localtime(e.time)), color)
        y -= 45
        rank += 1

def update():
    pass
