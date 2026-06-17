__all__ = ['test']  ##*指向test
def test(a, b):
    print(a+b)

def test2(a, b):
    print(a-b)

if __name__ == '__main__':  #仅在模块中测试
    test(1, 2)