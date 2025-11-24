def pickingNumbers(a):
    s = set(a)  
    length1 = 0
    longest = 0
    
    for i in s:
        new_list = list()
        for b in a:
            if b == i or b == i + 1:
                 new_list.append(b)
        length1 = len(new_list)
        
        if length1 > longest:
            longest = length1
    
    return longest
