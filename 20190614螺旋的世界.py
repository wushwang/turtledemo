"""
   螺旋的世界.py
   一个简单的程序，演示函数和coloradd命令的用法。
   本程序要用到coloradd模块,请在cmd里输入
   pip install coloradd进行安装。
   本程序运行的结果稍长，请耐心等待。
   运行结果是在屏幕上随机上很多螺旋。

"""
import turtle
from coloradd import *
from random import *


def draw_sprial():
    """画螺旋函数"""
    c = (1, 0, 0)  # RGB红色
    counter = randint(100, 250)  # 不定次数
    for i in range(counter):  # 迭代变量
        turtle.pencolor(c)  # 画笔颜色
        turtle.width(i / 100)  # 画笔笔宽
        turtle.fd(i / 100)  # 海龟前进
        turtle.rt(10)  # 海龟右转
        c = coloradd(c, 0.01)  # 颜色增加


width, height = 800, 600  # 定义宽高
screen = turtle.getscreen()  # 获取屏幕
screen.setup(width, height)  # 设置宽高
screen.title("多彩螺旋世界 www.lixingqiu.com")
screen.delay(0)  # 延时为0
screen.bgcolor("black")  # 背景为黑
turtle.hideturtle()  # 隐藏海龟
screen.tracer(0)  # 关闭动画
for i in range(2000):  # 迭代变量
    turtle.penup()  # 海龟抬笔
    x = randint(-width // 2, width // 2)
    y = randint(-height // 2, height // 2)
    turtle.goto(x, y)  # 定位坐标
    turtle.pendown()  # 海龟落笔
    draw_sprial()  # 画个螺旋
screen.update()  # 屏幕刷新
screen.mainloop()  # 入主循环