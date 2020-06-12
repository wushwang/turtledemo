"""本程序新建Durtle类，生成的拖动角色会换一个造型，松开它会隐藏"""
from turtle import *


class Durtle(Turtle):
    def __init__(self, images):
        Turtle.__init__(self, visible=False)
        self.begin_drag = 0  # 拖的标志
        self.penup()
        self.images = images  # 造型列表
        self.index = 0  # 初始造型索引
        self.amounts = len(images)  # 造型数量
        "设定初始造型"
        self.image = self.images[self.index]  # 当前造型
        self.shape(self.image)  # 设定造型
        self.st()  # 显示

        self.onrelease(self.act2)

    def alt_costume(self):
        "切换到下一个造型"
        if self.begin_drag == 0:
            self.index = self.index + 1
            self.index = self.index % self.amounts
            self.image = self.images[self.index]
            self.shape(self.image)
        self.begin_drag += 1

    def act1(self, x, y):
        """切换到下一个造型，定位到鼠标指针坐标"""
        self.alt_costume()
        self.goto(x, y)

    def act2(self, x, y):
        self.ht()
        self.goto(10000, 10000)
        self.begin_drag = 0
        # print("松开")

    def ondrag(self, btn=1, add=None):
        """重写ondrag，只会绑定一次"""
        Turtle.ondrag(self, self.act1, btn, add)


if __name__ == "__main__":
    images = "dog2-a.gif", "dog2-b.gif", "dog2-c.gif"
    width, height = 480, 360
    screen = Screen()
    screen.setup(width, height)
    screen.delay(0)
    screen.title("turtle的ondrag与类的继承练习Durtle类by李兴球")
    [screen.addshape(image) for image in images]
    d = Durtle(images)
    d.ondrag()
    screen.mainloop()
