def kangaroo(x1, v1, x2, v2):
    num = x2 - x1
    num2 = v1 - v2
    
    if (v1 - v2 == 0 and x2 != x1) or num * num2 < 0:
        return "NO"
        
    if num % num2 == 0:
        return "YES"
    else:
        return "NO"
    
