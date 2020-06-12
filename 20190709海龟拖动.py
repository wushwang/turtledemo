"""
   tkinter原生海龟示例_tkinter and RawTurtle example
   本程序新建tkinter窗口，然后新建一块300X300的画布，再在画布上放一只海龟。
   定义了几个事件，可以拖动海龟画画。
"""
import turtle
import tkinter

root = tkinter.Tk()  # 新建一个窗口
cv = tkinter.Canvas(root, width=300, height=300)
cv.pack()
t = turtle.RawTurtle(cv)  # 在画布上新建原生海龟
t.shape('turtle')
s = t.getscreen()  # 获取屏幕对象


def toggledown():
    """切换画笔状态"""
    if t.isdown():  # 如果是落笔则抬笔
        t.penup()
    else:
        t.pendown()


t.speed(0)
t.ondrag(t.goto)  # 设定拖动事件
s.onclick(t.goto)  # 设定单击事件
s.onkey(toggledown, 'space')  # 屏幕按键事件
s.listen()  # 监听键盘
s.mainloop()