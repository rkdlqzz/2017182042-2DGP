import turtle

cnt=0

while(cnt<6):
    turtle.penup()
    turtle.goto(0,cnt*100)
    turtle.pendown()
    turtle.forward(500)
    cnt+=1

cnt=0
turtle.left(90)

while(cnt<6):
    turtle.penup()
    turtle.goto(cnt*100,0)
    turtle.pendown()
    turtle.forward(500)
    cnt+=1

turtle.exitonclick()
