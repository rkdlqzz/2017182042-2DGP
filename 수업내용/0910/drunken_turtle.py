import turtle as t
import random as r

t.shape('turtle')
while 1:
    t.setheading(r.randint(0, 360))
    t.forward(r.randint(100, 200))
    t.stamp()