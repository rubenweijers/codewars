def is_pangram(s):
    alphabet = ["a", "b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for letter in s.lower():
        if letter in alphabet:
            alphabet.remove(letter)
    if alphabet == []:
        return True
    else:
        return False