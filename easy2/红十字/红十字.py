import turtle
t=turtle.Pen()
t.bgcolor("gray")   #  设置背景色
t.speed(0)  #设置速度
t.pencolor('red')  # 设置笔的颜色为红色
t.begin_fill()  # 开始填充
for x in range(4):   # 循环四次
  t.forward(200)     # 向前移动200步
  t.left(90)         # 左转90度
  t.forward(20)      # 向前移动20步
  t.left(90)         # 左转90度
  t.forward(200)     # 向前移动200步
  t.right(90)        # 右转90度
t.end_fill()   # 结束填充

  
