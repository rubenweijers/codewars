def josephus(items,k):
    """returns a Josephus permutation, taking as parameters
     the initial array/list of items to be permuted as if 
     they were in a circle and counted out every k places 
     until none remained."""
    l, index = [], 0

    while len(items) > 0:
        index = (index + (k - 1)) % len(items)
        l.append(items[index])
        items.remove(items[index])
    return(l)