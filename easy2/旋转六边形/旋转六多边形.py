import turtle
import random


# 设置画板背景色
turtle.bgcolor('black')
# 定义一只t的小海龟
t = turtle.Pen()
# 设置速度为20
t.speed(0)
t.color('lightblue')
# 定义变量，用于循环
x = 0
# 将六边形旋转18次
while x < 18:
    # 画一个正六边形
    for i in range(6):
        t.forward(100)
        t.right(60)
    # 每次旋转20度
    t.right(20)
    # 将x的值增加1
    x = (x + 1)
# 点击时关闭窗口
turtle.done()
