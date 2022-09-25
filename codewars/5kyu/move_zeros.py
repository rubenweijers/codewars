def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.append(i)
            lst.remove(i)
    return lst