def hello():
    return 'Hello, i am func "hello"'


def super_func(func):
    print('Hello, i am func "super_func"')
    print(func())


super_func(hello)
