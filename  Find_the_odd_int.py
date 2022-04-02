def find_it(seq):
    return next(el for el in seq if seq.count(el) % 2)
