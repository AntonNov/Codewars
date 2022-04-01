def find_it(seq):
    for el in seq:
        if seq.count(el) % 2:
            return el
