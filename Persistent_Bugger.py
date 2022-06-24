from functools import reduce


def persistence(num):
    cnt = 0
    list1 = list(map(int, str(num)))
    while len(list1) > 1:
        list1 = list(map(int, str(reduce(lambda x, y: x * y, list1))))
        cnt += 1
    return cnt
