import turtle
import cv2
import turtle as t


step = 2
turtle.bgcolor('pink')
t.speed(0)
t.penup()
t.goto((-200), 200)
t.pendown()
t.colormode(255)
img = cv2.imread('timg.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
for i in img:
    for j in i:
        t.color(j)
        t.begin_fill()
        for k in range(4):
            t.forward(step)
            t.left(90)
        t.end_fill()
        t.forward(step)
    t.setheading(270)
    t.penup()
    t.forward(step)
    t.setheading(180)
    t.forward((step * len(i)))
    t.setheading(0)
    t.pendown()

print(img)
