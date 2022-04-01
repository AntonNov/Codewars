def expanded_form(num):
    list1 = list(map(int, str(num)))
    cnt = 1
    for index, el in enumerate(list1):
        if el == 0:
            cnt += 1
            continue
        if index == 0:
            str1 = str(el * 10 ** (len(list1) - cnt))
        else:
            str1 += " + " + str(el * 10 ** (len(list1) - cnt))
        cnt += 1
    return str1
