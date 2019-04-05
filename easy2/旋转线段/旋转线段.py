import turtle

turtle.bgcolor('black')

t = turtle.Pen()  # 定义一只小海龟t
t.speed(0)           # 设置海龟的速度为0
t.pencolor('lightblue')

for i in range(180):     # 循环180次
    t.forward(100)   # 向前移动100步
    t.right(300)     # 向右转300步
    t.forward(50)    # 向前移动50步
    t.left(100)      # 左转100度
    t.forward(50)    # 向前移动50步
    t.right(100)     # 向右旋转100度

    t.penup()        # 抬笔
    t.setposition(0, 0)  #设置海龟的新位置（0,0）
    t.pendown()      # 落笔

    t.right(2)       # 右转2度

turtle.done()            
