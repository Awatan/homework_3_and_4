#Написать аналог функции len:
#Пример:
#>>my_len([1,2,3]
#3
#>>my_len(«hello»)
#5
a = [1, 2, 3, 4, 5, 6]


def my_len(a):
    i = 0
    for x in a:
        i = i + 1
    return i


print(my_len(a))


