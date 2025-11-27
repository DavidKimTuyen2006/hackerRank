def timeConversion(s):
    # Write your code here
    buoi = s[8:10]
    timeStr = s[0:8].split(":")
    timeLst = []
    
    for i in timeStr:
        tmp = int(i)
        timeLst.append(tmp)
        
    if buoi == "PM":
        if timeLst[0] != 12:
            timeLst[0] += 12
    else:
        if timeLst[0] == 12:
            timeLst[0] = 0
    kq = []
    
    for i in timeLst:
        tmp = f"{i:02d}"
        kq.append(tmp)
    return ":".join(kq)