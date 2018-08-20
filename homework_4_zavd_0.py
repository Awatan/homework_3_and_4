#dz_4 zavd_0
a = [1, 2, 3, 4, 5, 6]


def my_len(a):
    b = a
    for i in range(len(a)):
        b[i] = a[i] ** 2
    return a


print(my_len(a))
