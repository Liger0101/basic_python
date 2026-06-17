def str_reserve(s):
    """
    将字符串反转
    :param s:
    :return:
    """
    return s[::-1]

def substr(s, x, y):
    """
    按给定下标切片
    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]

if __name__ == '__main__':
    print(substr("sadhaidhai",1,4))