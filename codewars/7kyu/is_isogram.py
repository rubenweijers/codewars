def is_isogram(string):
    l = []
    for char in string.lower():
        if char not in l:
            l.append(char)
        elif char in l:
            return False
    return True