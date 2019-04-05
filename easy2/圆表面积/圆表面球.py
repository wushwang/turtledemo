import turtle


t=turtle.Pen()
# 设置画板背景色
turtle.bgcolor('black')
# 设置速度
t.speed(0)
# 设置笔的颜色
t.pencolor('green')
# 循环360次
for i in range(360):
    # 画圆，半径为i，依次从0-359中取值，正好360次
    t.circle(i)
    # 半径i为奇数时，左转
    if (i % 2 > 0) :
        t.left((i * 10))
        # 否则，右转
    else :
        t.right((i * 10))
