def func1(a, b, c):
    print(a, b, c)


def func2():
    print("func2 gets printed here")


def decorator_fun(func1):
    print("func2 gets called in decorator_func")


decorator_fun(func2)

