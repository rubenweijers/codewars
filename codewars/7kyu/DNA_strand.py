def DNA_strand(dna):
    l = ""
    for i in dna.upper():
        if i == "A":
            l += "T"
        elif i == "T":
            l += "A"
        elif i == "C":
            l += "G"
        elif i == "G":
            l += "C"
    return l