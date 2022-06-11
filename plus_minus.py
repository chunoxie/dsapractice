def plusMinus(arr):
    pos = zer = neg = 0
    n = len(arr)
    
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    
    txt = "Positive: {0:.2f} \nZero: {1:.2f} \nNegative: {2:.2f}".format(pos/n, zer/n, neg/n)
    print(txt)

a = [1,2,0,-3,-4]
plusMinus(a)