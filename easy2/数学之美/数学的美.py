import turtle
import random  # 导入海龟，随机工具箱

t = turtle.Pen()  # 生成一只海龟
turtle.bgcolor('black')
t.speed(0)  # 设置速度
for a in [360,500,600,700,900]: #设置初始的选择角度
    colors = ['red', 'cyan', 'green','pink', 'blue', 'yellow']  # 设置颜色
    for i in range(18):  # 循环
        while a > 0:
            t.fd(20)  # 向前移动20步
            t.lt(a)  # 左转a度
            a = a-2  # 每循环一次减2

        t.color(random.choice(colors))  # 设置笔的颜色
        a = 360  # 恢复a的初始值
        t.rt(20)  # 左转20度
    t.clear()
