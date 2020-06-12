"""
   旋转的赫兹.py
   三角函数与海龟画图示例程序
"""
import math
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.title("旋转的赫兹")
screen.tracer(0)
# 这个海龟叫萍乡
pingxiang = Turtle(visible=False)
pingxiang.pu()
pingxiang.setpos(0, 500)
pingxiang.pd()
pingxiang.setpos(0, -500)
pingxiang.pu()
pingxiang.setpos(-650, 0)
pingxiang.pd()
pingxiang.setpos(0, 0)
pingxiang.write("0", align="right", font=("Times New Roman", 14, "normal"))
pingxiang.setpos(650, 0)
# 这个海龟叫安源
anyuan = Turtle(visible=False)
for r in range(0, 600000):
    anyuan.clear()
    anyuan.pu()
    anyuan.setpos(-300 * math.cos(r * math.pi / 100), 300 * math.sin(r * math.pi / 100))
    anyuan.pd()
    anyuan.pencolor("red")
    for x in range(-300, 301):
        g = math.sin(x)
        t = math.cos(x)
        y = 100 * g * t * math.sin(2 * x**2 * math.pi / 100)
        tmp = r * math.pi / 100
        anyuan.setpos(x * math.cos(tmp) + y * math.sin(tmp), -x * math.sin(tmp) + y * math.cos(tmp))
    anyuan.pu()
    anyuan.setpos(-300 * math.sin(r * math.pi / 100), -300 * math.cos(r * math.pi / 100))
    anyuan.pd()
    anyuan.pencolor("blue")
    for y in range(-300, 301):
        c = math.sin(y)
        d = math.cos(y)
        x = 100 * c * d * math.cos(2 * y**2 * math.pi / 100)
        tmp = r * math.pi / 100
        anyuan.setpos(x * math.cos(tmp) + y * math.sin(tmp), -x * math.sin(tmp) + y * math.cos(tmp))
    screen.update()
screen.exitonclick()     # 单击关窗 