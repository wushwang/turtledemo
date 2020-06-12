"""请更改切片规则，让不同的海龟出列"""
from random import *
from time import sleep
from turtle import *


def write_index():
    """在海龟下面写上索引号"""
    i = 0
    # 遍历每只海龟
    for turtle in all_turtles:
        turtle.bk(60)
        rose.goto(turtle.position())
        rose.write(i, font=(None, 18, "normal"))
        turtle.fd(60)
        i = i + 1


def make_reg(maxnumber):
    """产生一个切片规则"""
    start = randint(0, maxnumber // 2)
    end = randint(0, maxnumber)
    step = randint(1, maxnumber // 2 - 1)
    return start, end, step


amounts = 10
color_list = ['red', 'orange', 'yellow', 'green', 'cyan',
              'blue', 'purple', 'brown', 'pink', 'white']
title = "切片教学演示动画"
screen = Screen()
screen.delay(10)
screen.title(title)
screen.bgcolor("black")

"rose是用来画不变字符串的海龟"
rose = Turtle(visible=False)  # 用来写切片规则的海龟对象
rose.speed(0)
rose.color("white")  # 颜色为白色
rose.penup()  # 抬笔
rose.goto(-180, 250)
rose.write(title, font=(None, 32, "normal"))
rose.goto(-80, -220)
rose.write("请单击屏幕", font=(None, 22, "normal"))
# 画中括号
rose.goto(-330, -25)
rose.write("[", font=(None, 52, "normal"))
rose.goto(320, -25)
rose.write("]", font=(None, 52, "normal"))
rose.goto(-330, -125)
rose.write("[", font=(None, 52, "normal"))
rose.goto(320, -125)
rose.write("]", font=(None, 52, "normal"))
rose.goto(-80, 100)
# 写中括号和规则
rose.write("起始:结束:步长", font=(None, 20, "normal"))

tom = Turtle(visible=False)  # tom用来写变化的切片规则
tom.penup()
tom.color("cyan")
tom.goto(-85, 140)

screen.turtles().pop()  # 把 tom 弹出
screen.turtles().pop()  # 把 rose 弹出

t = Turtle(shape='turtle')
t.shapesize(2.5, 2.5)
t.color(color_list[0])  # 设定颜色
t.penup()  # 抬笔
t.bk(270)  # 后退
t.sety(-90)
t.setheading(90)  # 朝上
t.initcors = t.position()  # 记录自己的初始坐标
for i in range(1, amounts):  # 迭代变量
    w = t.clone()  # 克隆一只海龟
    c = color_list[i % amounts]
    w.color(c)  # 设定颜色
    w.setx(t.xcor() + i * 60)  # 设置x坐标
    w.initcors = w.position()  # 记录自己的初始坐标
all_turtles = screen.turtles()  # 所有的海龟对象
print(len(all_turtles))
write_index()  # 在每只海龟下面写它的索引号


def change(x, y):
    tom.clear()
    start, end, step = make_reg(amounts)
    tom.write('[%d:%d:%d]' % (start, end, step), font=(None, 45, 'normal'))

    index = list(range(start, end, step))
    sleep(1)
    if len(index)!=0:
        for i in index:
            all_turtles[i].fd(90)
        sleep(1)
        for i in index:
            all_turtles[i].bk(90)


screen.onclick(change, btn=1, add=True)
screen.listen()
screen.mainloop()
