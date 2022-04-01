def solution(s):
    if len(s) % 2:
        s += "_"
    str1 = str()
    list1 = list()
    for index, el in enumerate(s):
        str1 += el
        if index % 2:
            list1.append(str1)
            str1 = str()
    return list1
