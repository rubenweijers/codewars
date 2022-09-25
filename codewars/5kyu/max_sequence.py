def max_sequence(arr):
    sum = 0
    maxsum = 0
    for i in arr:
        sum = max(0, sum + i)
        maxsum = max(maxsum, sum)
    return(maxsum)