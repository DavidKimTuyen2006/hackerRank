def breakingRecords(scores):
    # Write your code here
    result =[0,0]
    kmax = kmin = scores[0]
    for i in scores[1:]:
        if i > kmax:
            result[0] += 1
            kmax = i
        if i < kmin:
            result[1] += 1
            kmin = i
    return result
    