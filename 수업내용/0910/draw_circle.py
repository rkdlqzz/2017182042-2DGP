import turtle as t

for x, y, r in [(150, 150, 50), (-300, -300, 30), (100, 100, 40)]:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)
    t.write((x, y))