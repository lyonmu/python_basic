def testfunc():
    # 加
    print(2 + 3)
    # 减
    print(2 - 3)
    # 乘
    print(2 * 3)
    # 乘方
    print(2 ** 3)
    # 除
    print(2 / 3)
    # 整除
    print(2 // 3)
    # 取模
    print(2 % 3)
    # 位右移
    print(1 >> 1)
    # 位左移
    print(2 << 2)
    # 按位与
    print(0 & 1)
    # 按位或
    print(0 | 1)
    # 按位异或
    print(0 ^ 1)
    # 按位取反 x 的按位取反结果为 -(x+1)
    print(~1)
    # 比较运算符
    print(1 < 5)
    print(1 > 5)
    print(1 >= 5)
    print(1 <= 5)
    print(1 == 5)
    print(1 != 5)
    # not and or
    varnum = 1
    print(not varnum)
    print(True and False)
    print(True or False)


if __name__ == '__main__':
    testfunc()
