"""
   跳跃方块游戏.py
   屏幕右下方会不断地冒出尖峰，如果小方块碰到尖峰就会“死去”。
   按空格键可避开类峰。这个游戏没有设计封面和结尾，也没有配音。
   这里提供的代码只是抛砖引玉，读者可以脑洞大开，把它制作成一个完整的小游戏。 
"""
# 会员可直接向博主索取本作品源代码. 
from square import *
from spike import *


def overlape(spike, square):
    """spike只是一个三角形，这个函数判断
       spike的三个点是否在矩形中
    """
    # 确定矩形范围
    p = square.get_shapepoly()
    x1 = square.xcor() + p[2][0]  # 最左x坐标
    x2 = square.xcor() + p[1][0]  # 最右x坐标
    y1 = square.ycor() + p[0][1]  # 最下y坐标
    y2 = square.ycor() + p[1][1]  # 最上y坐标
    # 从get_shapepoly看出三个点的索引为1,2,3
    for i in range(1, 4):
        x, y = spike.get_shapepoly()[i]
        x = spike.xcor() + x
        y = spike.ycor() + y
        if x > x1 and x < x2 and y > y1 and y < y2:
            return True


width, height = 800, 600
screen = Screen()
screen.delay(0)
screen.setup(width, height)
screen.bgcolor("cyan")
screen.bgpic("blue sky.png")
screen.title("跳跃方块游戏 www.lixingqiu.com")
square = Square(4, 'orange')


def spawn_spike():
    Spike()
    screen.ontimer(spawn_spike, 1000)


spawn_spike()
screen.listen()
index = 0
running = True
while running:
    "循环检测尖峰的三个顶点有没有在矩形范围"
    spike = Spike.group[index % len(Spike.group)]
    if not spike.isvisible(): continue
    if overlape(spike, square):  # 如果其中一个点在
        running = False  # 那么游戏结束
        square.ht()  # 可以显示相关信息
    index = index + 1  # 下一个尖峰
    screen.update()  # 屏幕更新
screen.mainloop()