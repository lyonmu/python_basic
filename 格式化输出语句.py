def test_format():
    variable1 = 123
    variable2 = 11111111111111111111111111111111111111111111111111
    variable3 = 123.23
    variable4 = 'string'
    # 一个字符串可以使用某些特定的格式，随后， format 方法将被调用，使用这一方法中与之相应的参数替换这些格式。
    print('{0},{1}'.format(variable1, variable2))
    # 括号内的数字可以被省略
    print('{},{}'.format(variable1, variable2))
    print('wu{0}wuwu'.format(variable3))
    print('woshoi' + variable4 + 'dashjubdhjua')
    # 对于浮点数 '0.333' 保留小数点(.)后三位
    print('{0:.3f}'.format(1.0 / 3))
    # 使用下划线填充文本，并保持文字处于中间位置
    # 使用 (^) 定义 '___hello___'字符串长度为 11
    print('{0:_^11}'.format('hello'))
    # 基于关键词输出 'Swaroop wrote A Byte of Python'
    print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
    # end 指定其语句结束符,默认是换行结束符
    print('aaa', end='000')
    # 转义字符
    print("\t\\")
    # 原始字符串,在处理正则表达式时应全程使用原始字符串
    print(r"Newlines are indicated by \n")


if __name__ == '__main__':
    test_format()
