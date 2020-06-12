"""
   旋转黑洞.py
   按左右键操作小球逃出黑洞,碰到了黑洞的边框,那么计数器就会清零。

"""
import pygame
from frame import *
from rotator import *
from pygame.locals import *

# 会员可直接向博主索取本作品源代码.
width, height = 800, 600
title = "旋转黑洞 www.lixingqiu.com"
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
radius = 100  # 半径为100
center = width // 2, height // 2  # 中心点设为屏幕中央
旋转子 = Rotator(radius, center, (K_LEFT, K_RIGHT))

frame = Frame(screen)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT: running = False
    旋转子.update()
    frame.update()
    # 更新后进行基于mask的碰撞检测
    if pygame.sprite.collide_mask(旋转子, frame):
        print("飞天")
        frame.counter = 0
        frame.reset()

    screen.fill((0, 123, 0))
    screen.blit(frame.counter_image, frame.counter_rect)
    screen.blit(旋转子.image, 旋转子.rect)
    screen.blit(frame.image, frame.rect)
    pygame.display.update()
    clock.tick(30)
pygame.quit()
