import turtle

t=turtle.Pen()
t.bgcolor("black")   # 设置画板背景色为黑色
t.pencolor("white")  # 设置笔的颜色为白色
sides = 4            # 设置
colors = ["red", "green", "yellow", "purple", "blue", "orange"]  # 设置颜色列表
t.speed(0)           # 设置速度
for y in range(100): # 循环100次
    for x in range(24):  # 循环24次
        t.pencolor(colors[x % sides]) # 设置画笔的颜色
        t.forward(x)  # 向前移动x步
        t.left(x + 5) # 左转x+5度
    t.right(180)      # 右转180度
    for x in range(24):  # 循环24次
        t.pencolor(colors[x % sides])  # 设置笔的颜色
        t.forward(x)                   # 向前移动x步
        t.left(x + 5)                  # 左转x+5步
