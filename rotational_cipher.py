def rotate(text, key):
    # if 4<len(key)>5 or key[:3].upper()!="ROT" or not key[3:].isdigit() and (len(key) != 4 or len(key) != 5):
    #     return "Invalid Key"
    shift = int(key)
    if 0<shift>26:
        return "Invalid Shift" 
    if shift in (0,26):
        return text
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cypher = ""
    
    for char in text:
        if not char in alphabets and not char in alphabets.upper():
            print("here")
            cypher = cypher + char
            continue
        if char in alphabets:
            index = alphabets.index(char)
        if char in alphabets.upper():
            index = alphabets.upper().index(char)
        index = index + shift
        if index>25:
            total = index - 25
            if char in alphabets:
                cypher = cypher + alphabets[total-1]
            if char in alphabets.upper():
                cypher = cypher + alphabets.upper()[total-1]
        else:
            if char in alphabets:
                cypher = cypher + alphabets[index]
            if char in alphabets.upper():
                cypher = cypher + alphabets.upper()[index]
    return cypher


print(rotate("Let's eat, Grandma!",21))