def in_array(array1, array2):
    """Given two arrays of strings a1 and a2, 
    return a sorted array r in lexicographical order 
    of the strings of a1 which are substrings of strings of a2"""
    
    l = []
    for i in array1:
        for j in array2:
            if i in j and i not in l:
                l.append(i)
    l.sort()
    return(l)