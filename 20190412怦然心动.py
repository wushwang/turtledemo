"""怦然心动.py
形状列表是海龟画图内置形状（造型）的一个列表，存储了海龟的形状，每个形状是一个多边形。
它的所有顶点坐标可以通过海龟的get_shapepoly命令获取。如以下代码获取默认的海龟对象的顶点坐标
>>> import turtle
>>> turtle.get_shapepoly()
((0, 0), (-5, -9), (0, -7), (5, -9))
通过屏幕的addshape命令可以添加新的造型，下面新的造型名称为line，值就是p列表。
例：
 p = [(0,0),(10,10)]，通过屏幕的addshape('line',p)就能在形状列表里添加这个名为
line的形状。获取形状列表用屏幕的 getshapes命令。
内置的形状列表为： ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
"""
from turtle import *
from time import sleep


def rightmove():
    for i in range(200):
        t.right(1)
        t.forward(1)


screen = Screen()
screen.setup(480, 360)
screen.bgcolor("black")
screen.title("怦然心动 by lixingqiu")
t = Turtle(shape="blank")
t.penup()
t.color("magenta")
screen.tracer(False)  # 加这句不会显示画的过程
# 下面是画心的代码
t.begin_poly()  # 开始记录顶点坐标
t.left(140)
t.forward(111.65)
rightmove()
t.left(120)
rightmove()
t.forward(111.65)
t.end_poly()  # 结束记录顶点坐标
p = t.get_poly()  # 得到刚画的多边形的顶点坐标
screen.update()
screen.tracer(True)  # 重新显示来的过程
screen.addshape('heart', p)  # 把画好的形状添加到形状列表
t.shape('heart')  # 设定海龟的造型为心形
t.setheading(90)  # 设置朝向
t.bk(50)  # 倒退100
t.clear()  # 清空所画图形
x = 0
while True:
    x = x + 1
    scale = y = 10 - abs(10 - x % 20)
    s = ((scale + 1) / 10.0)
    t.shapesize(s, s)
    sleep(0.01)
    screen.update()