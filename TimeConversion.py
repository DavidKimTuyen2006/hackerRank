def timeConversion(s):
    day_time = s[-2]
    time = s[0:2]
        
    if day_time == 'P':
        if time == "12":
            return s[0:8]
        else:
            time = int(time) + 12
            time = str(time) 
            return time + s[2:8]
         
    elif day_time == 'A':
        if time == "12":
            time = "00"
            return time + s[2:8]
        else:
            return time + s[2:8]
