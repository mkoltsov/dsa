def fltat(s:str)->str:
    print(11111)
    seen=set()

    for i in s:
        print(s)
        if i in seen:
            return i
        seen.add(i)
    print(s)    
    return " "

print(fltat("abracadabra"))    
          