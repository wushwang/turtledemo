import turtle


def _circle(x,y,color,r):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

t = turtle.Pen()
t.speed(6)
turtle.bgcolor('black')
_circle(200, 0, 'red', 200)
_circle(175, 0, 'white', 175)
_circle(150, 0, 'red', 150)
_circle(125, 0, 'blue', 125)
t.fillcolor('white')
t.pencolor('white')
t.penup()
t.goto((-118), 38)
t.setheading(0)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(238)
    t.right(144)
t.end_fill()
t.hideturtle()
turtle.done()
