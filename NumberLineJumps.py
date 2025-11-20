def kangaroo(x1, v1, x2, v2):
    result = "NO"
    for i in range (10000):
        if ((x1 + v1*i) == (x2 + v2*i)):
            result = "YES"
            return result
    return result
