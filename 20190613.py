"""
   哪吒拼图核心源代码.py
   方块类Block的定义模块
"""
import os
from time import sleep
from splitimage import *
from random import shuffle
from tkinter import messagebox
from turtle import Turtle, Screen


class Block(Turtle):
    """方块类，一个方块就是一张切好的图片的封装。当新建一个方块时，
       initcors属性会记住它的应该呆的坐标，而coordinates[i]则是随
       机的一个坐标，两个坐标是不同的。 image就是它的外形。
       它的action方法是单击它后的响应，check_all_picture是检测每张
       图片有没有归位。
    """
    switching = False
    clicked = []  # 记录被第一个被单击的角色的列表
    images = []  # 类变量，记录所有的方块
    success_flag = False  # 过关标志

    def __init__(self, image, coordinates, index, i):
        """image:外形图,coordinates:坐标表,
           index:初始坐标索引,i:起始坐标索引
        """
        Turtle.__init__(self, shape=image)
        self.initcors = coordinates[index]  # 初始坐标,归位后的坐标
        self.penup()  # 抬笔
        self.onclick(self.action)  # 单击绑定action
        Block.images.append(self)  # 添加到图像列表中
        self.goto(coordinates[i])  # 定位到打乱了的位置

    def action(self, x, y):
        """单击方块时的动作,基本原理,首先记住第一次单击的方块。
           ，等第二次单击时，就能交换它们的坐标了。
        """

        if Block.switching: return  # 防止在移动过程中被单击
        Block.switching = True
        if Block.clicked == []:  # 如果是第一次单击
            Block.clicked.append(self)  # 把自己放到列表中
        else:
            first_block = Block.clicked.pop()  # 弹出第一次单击的方块
            second_xy = self.position()  # 保存好自己的坐标
            self.goto(first_block.position())  # 第二次单击的角色定位
            first_block.goto(second_xy)  # 第一个角色再次定位
        "每单击一次就进行一次遍历，检查每个图片有没有归位。"
        Block.check_all_picture()
        Block.switching = False
        self.screen.title(str(Block.switching))

    @staticmethod
    def check_all_picture():
        """检测每个方块是否归位"""
        counter = 0
        for image in Block.images:
            "检测每部分图是否归位，每块图的当前坐标和初始坐标进行比较"
            c1 = abs(image.xcor() - image.initcors[0]) < 5
            c2 = abs(image.ycor() - image.initcors[1]) < 5
            if c1 and c2:
                counter = counter + 1
                continue
            else:
                break
        print(counter)
        if counter == len(Block.images):
            messagebox.showinfo("恭喜，恭喜", "成功啦")
            Block.success_flag = True
            return True


if __name__ == "__main__":
    cors = [(100, 100), (-100, -100), (-100, 100), (100, -100)]

    screen = Screen()
    screen.delay(20)
    screen.bgcolor("gray")

    redblock = Block('square', cors, 0, 3)
    redblock.shapesize(8, 8)
    redblock.color("red")

    orangeblock = Block('square', cors, 1, 2)
    orangeblock.shapesize(8, 8)
    orangeblock.color("orange")
    yellowblock = Block('square', cors, 2, 0)
    yellowblock.shapesize(8, 8)
    yellowblock.color("yellow")

    greenblock = Block('square', cors, 3, 1)
    greenblock.shapesize(8, 8)
    greenblock.color("green")