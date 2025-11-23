def timeConversion(s):
    day_time = s[-2]
    time = s[0:2]
    
    if day_time == 'P' and time == "12":
        return s[0:8]
    elif day_time == 'A' and time == "12":
        time = "00"
        return time + s[2:8]
        
    elif day_time == 'P':
        time = int(time) + 12
        time = str(time) 
        return time + s[2:8]
         
    elif day_time == 'A':
        return time + s[2:8]
