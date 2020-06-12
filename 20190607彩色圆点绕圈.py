"""彩色圆点绕圈图_Python海龟画图练习"""
import turtle
colors = ['red','orange','yellow','green','cyan','blue','purple']
amounts = len(colors)
screen = turtle.getscreen()
screen.title("彩色圆点绕圈图")
screen.bgcolor("red")
screen.setup(640,480)
screen.delay(0)
turtle.penup()
for x in range(40):
    for i in range(amounts):
        turtle.color(colors[i])
        turtle.dot(i * 10 + 10)
        turtle.fd(30)
    turtle.bk(210)
    turtle.right(9)
screen.exitonclick()         # 单击关闭窗口