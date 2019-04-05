import turtle


# 定义一只新画笔
t = turtle.Pen()
# 循环5次
t.fillcolor("#cc66cc")
t.begin_fill()
for i in range(5):
    # 每次向前移动144步
    t.forward(144)
    # 每次旋转144度
    t.right(144)
t.end_fill()
# 阻止画完之后窗口退出
turtle.done()
