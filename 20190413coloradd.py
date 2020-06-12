"""颜色增加与颜色设定命令,用来在海龟画图中做颜色渐变。
   作者:李兴球 2019/4/13晚更新
   本程序定义了两个函数，coloradd是用来增加颜色的，colorset是把一个整数转换成rgb三元色值。
"""
import colorsys


def coloradd(color, dh):
    """颜色增加
       color是三元组,分别为0-1之间的浮点数。
       此函数把颜色转换成hls模式,对色度h进行增加色度dh的操作
       然后转换回去,dh是小于1的浮点数。       
    """
    if len(color) == 3:
        h, l, s, = colorsys.rgb_to_hls(color[0], color[1], color[2])
        h = h + dh
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return r, g, b
    else:
        return color


addcolor = coloradd  # 定义别名


def colorset(color):
    """设定颜色,color范围为1到360
       把一个整数转换成三元色值
    """
    color = color % 360
    color = color / 360.0
    r, g, b = colorsys.hsv_to_rgb(color, 1.0, 1.0)

    return r, g, b


setcolor = colorset  # 定义别名
if __name__ == "__main__":
    color = (1, 0, 0)
    color = coloradd(color, 0.001)
    print(color)
    print()
    color = (1, 0, 0)
    for i in range(256):
        color = coloradd(color, i / 255)
        r = int(color[0] * 255)
        g = int(color[1] * 255)
        b = int(color[2] * 255)
        print(r, g, b)

    input("颜色增加与颜色设定命令,作者:李兴球,请按回车键结束测试.")