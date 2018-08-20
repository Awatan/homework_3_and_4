a = [1, 2, 3, 4, 5, 6]


def my_reversed(a):
    b = [0]
    for i in range(len(a)):
        b[i] = a[::-1]
        return b


print(my_reversed(a))
