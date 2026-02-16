def gradingStudents(grades):
    # Write your code here
    ans = []
    n = len(grades) 
    for i in range(0, n):
        if grades[i] < 38: 
            ans.append(grades[i])
        else:
            up = grades[i]
            for j in range(0,2):
                up+=1
                if up%5 == 0:
                    ans.append(up)
                    break
            if up % 5 != 0:
                ans.append(grades[i])
    return ans 
    