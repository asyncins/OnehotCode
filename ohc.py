import numpy


# 数字与大写字母混合
NUMBER = [str(_) for _ in range(0, 10)]
LETTER = [chr(_).upper() for _ in range(97, 123)]
CHARACTER = {v: k for k, v in enumerate(NUMBER + LETTER)}

# 验证码字符数
CAPTCHA_NUMBER = 6


def one_hot_encode(value):
    """编码，将字符转为独热码
    vector为独热码，order用于解码
    """
    order = []
    shape = CAPTCHA_NUMBER * len(CHARACTER)
    vector = numpy.zeros(shape, dtype=float)
    for k, v in enumerate(value):
        index = k * len(CHARACTER) + CHARACTER.get(v)
        vector[index] = 1.0
        order.append(index)
    return vector, order


def one_hot_decode(value):
    """解码，将独热码转为字符
    """
    res = []
    for ik, iv in enumerate(value):
        val = iv - ik * len(CHARACTER) if ik else iv
        for k, v in CHARACTER.items():
            if val == int(v):
                res.append(k)
                break
    return "".join(res)


if __name__ == '__main__':
    """ Example """
    code = '0A2JYD'
    vec, orders = one_hot_encode(code)
    print('将 %s 进行特征数字化处理\n' % code)
    print('特征数字化结果：%s\n' % vec)
    print('字符位置：%s\n' % orders)
    print('根据特征数字化时的字符位置进行解码，解码结果为：%s' % one_hot_decode(orders))

