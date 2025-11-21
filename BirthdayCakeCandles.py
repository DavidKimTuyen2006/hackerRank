def birthdayCakeCandles(candles):
    candles.sort()
    result = 0
    for i in candles:
        if i == candles[-1]:
            result += 1
    return result
