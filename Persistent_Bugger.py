from numpy import product


def persistence(num):
    cnt = 0
    list1 = list(map(int, str(num)))
    while len(list1) > 1:
        list1 = list(map(int, str(product(list1))))
        cnt += 1
    return cnt
