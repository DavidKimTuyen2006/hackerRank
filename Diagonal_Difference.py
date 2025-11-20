def diagonalDifference(arr):
    num1 = 0
    num2 = 0
    n = len(arr)
    for i in range (n):
        num1 += arr[i][i]
        num2 += arr[n - 1 - i][i]
        
    return (abs(num1 - num2))
    
