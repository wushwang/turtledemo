"""
   用到了勾股定理的简易海龟图章图形
"""
from turtle import *
from random import *
radius = 200
colors = ['red','orange','yellow','green',
          'cyan','blue','purple','pink',
          'brown','magenta','gray']
t = Turtle(shape='turtle')
screen = t.getscreen()
screen.delay(0)
t.penup()
while True:
     x = randint(-radius,radius)
     y = randint(-radius,radius)
     if (x*x+y*y)<= radius*radius:
          c = choice(colors)
          t.color(c)
          t.goto(x,y)
          t.stamp()