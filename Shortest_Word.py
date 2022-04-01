def find_short(s):
    list1 = str(s).split()
    size = len(list1.pop(0))
    for word in list1:
        size = min(len(word), size)
    return size
