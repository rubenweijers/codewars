def scramble(s1, s2):
    """Scramble returns true if a portion of s1 characters
    can be rearranged to match s2, otherwise returns false"""
    for i in set(s2):
        if s1.count(i) < s2.count(i):
            return False
    return True