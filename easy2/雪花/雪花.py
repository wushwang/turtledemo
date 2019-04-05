import turtle
import random

def branch():  # 定义一个画分支的方法
    for i in range(3):
        for j in range(3):
            t.forward(30)
            t.backward(30)  # 向后退30步
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90)
    t.forward(90)

t = turtle.Pen()  # 定义名字为t的海龟
turtle.bgcolor("grey")  # 设置画板颜色为grey
colours = ["cyan", "purple", "white", "blue"]  # 定义颜色列表
t.penup()  # 抬笔
t.forward(90)  # 向前移动90步
t.left(45)  # 向左移动45步
t.pendown()  # 落笔
for k in range(8):
    branch()
    t.left(45)
