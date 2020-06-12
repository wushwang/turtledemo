"""
   海龟图腾花.py
"""
import turtle
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple',
          'brown', 'pink', 'white', 'gray', 'magenta', 'black']
screen = turtle.getscreen()
screen.bgcolor('gray')
screen.delay(0)
turtle.penup()
turtle.setx(-150)
turtle.width(20)
turtle.speed(0)
turtle.pendown()
while True:
    for x in range(12):
        turtle.color(colors[x%len(colors)])
        turtle.fd(6*x)
        turtle.right(x)
    turtle.left(x+210)