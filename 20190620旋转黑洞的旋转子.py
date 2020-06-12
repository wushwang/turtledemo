"""
   rotator.py
   旋转黑洞游戏的旋转子,类名为Rotator,
   实例化后,按左右键会绕中心点旋转。
"""
import math
import pygame
from pygame.locals import *


class Rotator(pygame.sprite.Sprite):
    def __init__(self, radius, center, keys):
        """
           radius：旋转半径，
           center：旋转中心点，
           keys：按键表(左右按键)
        """

    # 练习，请根据上下文把本代码补全
    def set_pos(self):
        """设置坐标"""
        a = math.radians(self._angle)
        x = self.center[0] + self.radius * math.cos(a)
        y = self.center[1] - self.radius * math.sin(a)
        self.rect.center = x, y

    def update(self):
        """先进行按键检测，再更新坐标"""
        self.keys_check()
        self.set_pos()

    def keys_check(self):
        """按键检测"""
        keys = pygame.key.get_pressed()
        if keys[self.keys[0]]:
            self._angle += 1
        elif keys[self.keys[1]]:
            self._angle -= 1


def main():
    """主要函数"""

    width, height = 800, 600
    title = "旋转黑洞的Rotator类测试程序"

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    radius = 100  # 半径为100
    center = width // 2, height // 2  # 中心点设为屏幕中央
    旋转子 = Rotator(radius, center, (K_LEFT, K_RIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT: running = False
        旋转子.update()
        screen.fill((0, 123, 0))
        screen.blit(旋转子.image, 旋转子.rect)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()