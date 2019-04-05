import turtle


t = turtle.Pen()
# 设置海龟的速度
t.speed(0)
# 设置笔的颜色
t.pencolor('pink')
#  设置画板背景色
turtle.bgcolor('black')
#  循环150次，x依次为0-149
for x in range(1500):
    # 向前移动x步
    t.forward((x * 2))
    # 左转95度
    t.left(95)
