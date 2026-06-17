def print_file_info(file_name):
    """
    将指定文件中的内容输出到控制台
    :param file_name:
    :return:
    """
    f = None
    try:
        f = open(file_name,"r",encoding="utf-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(e)
    finally:
        if f:   #若变量是None，表示False,有内容是True
            f.close()

def append_to_file(file_name,content):
    """
    追加数据
    :param file_name:
    :param content:
    :return:
    """
    f = open(file_name,"a",encoding="utf-8")
    f.write(content)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("D:/python1.txt")