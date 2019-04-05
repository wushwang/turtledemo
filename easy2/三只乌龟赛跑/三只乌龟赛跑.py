import turtle
import random


#定义三只画笔
t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
#设定每只画笔的属性
t1.pencolor("#33ff33")
t2.pencolor("#ff0000")
t3.pencolor("#000099")
t1.goto((-300), 100)
t2.goto((-300), 0)
t3.goto((-300), (-100))
all_turtles = [t1,t2,t3]
while True:
    for t in all_turtles:
        rand_dist = random.randint(1, 40)
        t.forward(rand_dist)
