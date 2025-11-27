def birthdayCakeCandles(candles):
    max = 0
    for i in candles:
        if i > max:
            max = i
    ans = 0
    for i in candles:
        if i == max:
            ans += 1
    return ans
