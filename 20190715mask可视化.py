"""
   mask碰撞检测原理示例程序。mask是由010101...组成的。1代表相应的像素点不透明。0代表相应坐标的像素点是透明，即那里是空的。
"""
import pygame
pygame.init()
screen = pygame.display.set_mode((480,360))
width,height = 50,50
x1,y1 = 100,100
sur1 = pygame.Surface((width,height)).convert_alpha()
sur1.fill((255,100,100,0))                # 最后的0代表完全透明
sur1_rect = sur1.get_rect(topleft=(x1,y1))  # 定位
sur1_mask = pygame.mask.from_surface(sur1)  # 取掩膜
print(sur1_mask.get_at((1,1)))              # 取(1,1)掩膜值
screen.blit(sur1,sur1_rect)
x2,y2 = 120,128
sur2 = pygame.Surface((width,height)).convert_alpha()
sur2.fill((100,100,255))
sur2_rect = sur2.get_rect(topleft=(x2,y2)) # 定位
sur2_mask = pygame.mask.from_surface(sur2)  # 取掩膜
screen.blit(sur2,sur2_rect)                 # 贴到屏幕
pygame.display.update()
offset = x2 - x1 , y2 - y1
p = sur1_mask.overlap(sur2_mask,offset)
print(p)

# 在上面的程序中如果sur1是完全透明的，那么它就碰不到sur2了。
#
# mask说明：
# mask是用来表示图像部位哪些可以“碰撞”的部分,哪些是不接受“碰撞的部分的一种方式。
#
# 如果一个图像不是每像素格式，在没有colorkey的情况下，它全部是不透明的。
# 从surface创建的mask的每一个位的值将都是1，表示所有像素能接受“碰撞”检测。
#
# 如果设置了colorkey，那么和colorkey这种颜色相等的颜色所在的位都将是1，否则是0。
#
# 如果是每像素模式，colorkey是无意义的。这个时候当它的alpha值大于127的时候，
# 此像素点的mask值将是1，否则是0。127是设置一个像素位置的mask值是否为1的阈值。
#
# 通俗地说，mask就是很多标志，标为1的地方代表图像的这个地方的碰撞有效，0代表此处碰撞无效。
