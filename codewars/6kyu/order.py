def order(sentence):
    split = sentence.split(" ")
    newstring = ""
    count = 1
    while len(newstring) < len(sentence):
        for word in split:
            strcount = str(count)
            if strcount in word:
                newstring += word
                newstring += " "
                count+=1
    return newstring.strip()