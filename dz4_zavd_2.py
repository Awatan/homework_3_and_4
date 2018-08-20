a = [1, 2, 3, 4, 5, 6]


def my_next(a):
    b = [0]
    b[0] = a[-1]
    b.extend(a)
    del b[-1]
    return b


print(my_next(a))
