def is_square(n):
    if n < 0:
        return False
    return n == (int(n ** 0.5)) ** 2
