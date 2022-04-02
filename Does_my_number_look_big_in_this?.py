def narcissistic(value):
    summa, dgr = 0, 0
    while summa < value:
        summa = sum(el ** dgr for el in map(int, str(value)))
        dgr += 1
    return summa == value
