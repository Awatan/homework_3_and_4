a = [1, 2, 3, 4, 5, 6]


def my_two(a):
    b = a
    for i in range(len(a)):
        b = [i for i in a if not int(i) % 2]
        b = b[0] + b[1]
    return b


print(my_two(a))
