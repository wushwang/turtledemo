"""
   python纯画笔动画弹球.py
   注意本程序虽然海龟移动了,但重点在于演示它画的画（打的圆点）在移动,
   所以叫纯画笔动画。本程序是动画原理演示动画。
"""
import time
import turtle
from random import randint
ball = turtle
width,height = 960,720
screen = ball.getscreen()
screen.bgcolor("black")
screen.title("纯画笔动画弹球")
screen.setup(width,height)
screen.tracer(0)       # 关闭自动刷新
ball.color('cyan')
ball.up()              # 抬笔
ball.ht()              # 和本身形状无关，所以隐藏
diameter = 100         # 设定直径为100
radius = diameter//2   # 半径
dx = randint(-10,10)   # 单位水平位移
dy = randint(-10,10)   # 单位垂直位移
while True:
    ball.clear()       # 擦除以前所画的一切
    # 下面是修改坐标
    x = ball.xcor() + dx
    y = ball.ycor() + dy
    ball.goto(x,y)
    ball.dot(diameter)  # 在此坐标画个圆
    if (x + radius) > width//2 or (x-radius) <= -width//2:
        dx = -dx
    if (y + radius) > height//2 or (y-radius) <= -height//2:
        dy = -dy
    # 最后重画
    screen.update()
    time.sleep(0.01)