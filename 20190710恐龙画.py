"""
   海龟画恐龙字符画,本程序会根据字符列表绘制作一个恐龙像素画
"""
import tkinter as tk
from turtle import Turtle, Screen
character_list = [
    ",,,,,,,,,,,,,,,,,,,,,,,,,",
    ",,,,,,****,,,,,,,,,*,,,,,",
    ",,,,,*!!!!*,,,,,,,*¤*,,,,",
    ",,,,*!!!!!!*,,,,,,*¤¤*,,,",
    ",,,,*!!!!!!*,,,,,,*¤¤*,,,",
    ",,,*!!!!!!!!*,,,,*¤¤¤¤*,,",
    ",,*!!!!,*!!!*,,,,*¤¤%¤*,,",
    ",,*!!!!**!!!!*,,,*¤%%¤*,,",
    ",,*!!!!**!!!!*,,,,*%**,,,",
    ",,,*!!!!!!!!!!*,,,*!*,,,,",
    ",,,,**!!!!!!!!!*,*!!*,,,,",
    ",,,,,,***!!*!!!**!!*,,,,,",
    ",,,,,,,*%%*!!!!!*!!*,,,,,",
    ",,,,,,,*%%%**!!!*!*,,,,,,",
    ",,,,,,*,*%%%!!!!**,,,,,,,",
    ",,,,,,,***%%!!!**,,,,,,,,",
    ",,,,,,,,,,***!**,,,,,,,,,",
    ",,,,,,,,,,,*,!,*,,,,,,,,,",
    ",,,,,,,,,,,,****,,,,,,,,,",
    ",,,,,,,,,,,,,,,,,,,,,,,,,"
]
colors = {
            ","  :  "white",
            "*"  :  "black",
            "!"  :  "orange",
            "¤"  :  "red",
            "%"  :  "yellow"
}
tk.ROUND = tk.BUTT
SCALE = 5 
screen = Screen()
screen.delay(0)
screen.title("海龟画恐龙字符画")
width = screen.window_width() / SCALE 
height = screen.window_height() / SCALE
screen.setworldcoordinates(-width//2, -height//2, width//2, height//2)
t = Turtle(visible=False)
t.speed('fastest')          # 最快的速度
t.width(SCALE)              # 设定画笔宽度
r = len(character_list[0])  # 每行字符数
# 下面是一行一行的扫描字符把它画出来
for row in character_list:
    t.pendown()
    for char in row:
        t.pencolor(colors[char])
        t.forward(1)
    t.penup()
    t.backward(r)
    t.right(90)
    t.forward(1)
    t.left(90)
screen.exitonclick()