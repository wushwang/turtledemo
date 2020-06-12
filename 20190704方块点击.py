"""
   pygame的方块类鼠标单击示例样本程序.py
"""
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SIZE = WIDTH, HEIGHT = 480, 360


class Square(pygame.sprite.Sprite):
    """
       定义类，继承自Sprite类
    """

    def __init__(self, pos, color, size):
        """
           pos：方块中心点坐标
           color：颜色
           size：宽高
        """
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.size = size
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def check_click(self, pos):
        """
           检测pos是否在矩形内
        """
        if self.rect.collidepoint(pos):
            print("\n你单击了", self.color, "颜色的方块")
            print("它的宽高是：", self.size)


def main():
    """
       主函数
    """
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("pygame的方块类鼠标单击示例样本程序")
    # 这个红色广块叫安源
    anyuan = Square((10, 10), RED, (100, 100))
    # 下面的方块叫北桥          
    beiqiao = Square((100, 100), GREEN, (50, 50))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(anyuan, beiqiao)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or  (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for s in all_sprites:
                    s.check_click(event.pos)

        all_sprites.update()

        screen.fill(BLACK)
        all_sprites.draw(screen)  # 在screen上画方块
        pygame.display.update()
    pygame.quit()  # 退出pygame


if __name__ == "__main__":
    main()
