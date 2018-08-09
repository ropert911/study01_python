"""fffffffffffff"""

def run(f):
    """包装函数，当执行的函数需要进行异常捕获的时候，可以使用@run进行修饰，确保程序正常退出，并且将异常日志写入日志文件

    :param f: 需要被包装的函数对象
    :return: 包装函数对象
    """
    print("wrapper are in %s %s" % (__name__, f.__name__))

    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print('Exception {}: {}, {}'.format(f.__name__, type(e), e))

    return wrapper
