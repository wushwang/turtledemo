import turtle


def square():  # 定义一个画正方形的方法
    t.color('red')
    t.begin_fill()
    for i in range(4):  # 旋转4次
        t.forward(100)  # t向前移动100步
        t.right(90)  # 向右转90度
    t.end_fill()


turtle.bgcolor('black')
t = turtle.Pen()  # 生成一只小画笔，名字为t
t.speed(0)  # 设置t的速度
t.color('lightblue')
for i in range(100):  # 循环100次
    square()  # 每次画一个正方形
    t.right(21)  # 向右旋转21度
t.done()
