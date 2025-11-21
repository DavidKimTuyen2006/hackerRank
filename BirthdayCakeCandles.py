def birthdayCakeCandles(candles):
    s = sorted(candles)
    result = 0
    for i in s:
        if i == s[-1]:
            result += 1
    return result
