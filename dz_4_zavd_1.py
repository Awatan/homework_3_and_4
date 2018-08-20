a = [1, -2, 3, -4, 5, 6]


def my_len(a):
    for i in range(len(a)):
        if a[i] < 0:
            a[i] = a[i+1]
    return a


print(my_len(a))
