"""
   毛毛虫动画.py
   用turtle模块制作的一个蓝色的毛毛虫在沿着正方形轨迹移动.
   while循环示例,计数器示例。
"""
from turtle import *
t = Turtle()
t.shape("turtle")
t.color("blue")
t.penup()
for x in range(10):
    t.stamp()
c = 0
while True:
    counter = 0
    while counter < 10:
        t.stamp()
        t.fd(10)
        t.clearstamps(1)
        counter = counter + 1
    t.right(90)