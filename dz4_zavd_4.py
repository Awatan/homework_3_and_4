a = [1, -2, 3, -4, 5, 6]


def my_zero(a):
    for i in range(len(a)):
        if i % 2 != 0:
            a[i] = 0
    return a


print(my_zero(a))
