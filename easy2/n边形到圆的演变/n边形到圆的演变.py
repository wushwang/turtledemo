import turtle


#生成一支画笔
t = turtle.Pen()
# 抬笔
t.penup()
t.speed(0)
# 移到（-100，-200）
t.goto((-100), (-200))
# 落笔
t.pendown()
# 设置画笔的大小为3
t.pensize(3)
# 设置画笔的颜色为绿色.
t.pencolor('green')
# 循环，sdies依次从3-20中取值
for sides in range(3,21):
    # 开始填充
    t.begin_fill()
    # 画sides边形，例如sides=3时，正三角形
    for i in range(sides):
        # 向前移动100步
        t.forward(100)
        # 旋转360/sides度，例如正三角形360/3=120度
        t.left((360 / sides))
