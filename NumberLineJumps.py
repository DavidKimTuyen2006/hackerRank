def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 == x2 and v1 == v2:
        return "YES"
    elif x1 == x2 and v1 != v2:
        return "NO"
    elif v1 == v2 and x1 != x2:
        return "NO"
    else:
        faster = slower = 0
        fplace = splace = 0
        if v1 > v2:
            faster = v1
            fplace = x1 + v1
            slower = v2
            splace = x2 + v2
        else:
            faster = v2
            fplace = x2 + v2
            slower = v1
            splace = x1 + v1
        while True:
            if splace > fplace:
                splace += slower
                fplace += faster
            elif splace == fplace:
                return "YES"
            else:
                return "NO"   