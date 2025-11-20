def plusMinus(arr):
    positive = negative = zero = 0;
    
    n = len(arr)
    
    for i in range(n):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1
            
    print(f"{positive / n:.6f}")
    print(f"{negative / n:.6f}")
    print(f"{zero / n:.6f}")
