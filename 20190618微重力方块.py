"""
   微重力方块.py
   程序运行后,按上下左右键操作小方块,它好像在太空中一样。
   一不小心就会在惯性的作用下一直滑动。读者可以把本程序改
   造成一个小游戏哦。练习是完成move方法.
"""
from turtle import *


class Square(Turtle):
    def __init__(self, keys, colour):
        """keys：按键列表，colour：颜色"""
        Turtle.__init__(self, shape='square')
        self.keys = keys  # 上下左右键
        self.color(colour)
        self.penup()
        self.dx = 0
        self.dy = 0
        self.screen.onkeypress(self.moveup, keys[0])
        self.screen.onkeypress(self.movedown, keys[1])
        self.screen.onkeypress(self.moveleft, keys[2])
        self.screen.onkeypress(self.moveright, keys[3])
        self.move()

    def move(self):
        """不断地移动"""
        pass  # 请结合上下文自行编写本段代码
        # 会员可直接向博主索取源代码,其它文章省略的代码也一样.

    def moveup(self):
        self.dy = self.dy + 0.1

    def movedown(self):
        self.dy = self.dy - 0.1

    def moveleft(self):
        self.dx = self.dx - 0.1

    def moveright(self):
        self.dx = self.dx + 0.1


if __name__ == "__main__":
    screen = Screen()
    screen.delay(0)
    screen.bgcolor("black")
    screen.title("微重力方块")
    keys = ['Up', 'Down', 'Left', 'Right']
    square = Square(keys, 'cyan')
    screen.listen()
    screen.mainloop()