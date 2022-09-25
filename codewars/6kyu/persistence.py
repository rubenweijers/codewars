def persistence(n):
    product = 1
    count = 0

    while len(str(n)) > 1:
        product = 1
        for i in str(n):
            product *= int(i)
        count += 1
        n = product
    return count