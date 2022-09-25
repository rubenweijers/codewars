def xo(s):
    x = []
    o = []
    for i in s.lower():
        if i == 'x':
            x.append(x)
        elif i == 'o':
            o.append(i)
    if len(x) == len(o):
        return True
    else:
        return False