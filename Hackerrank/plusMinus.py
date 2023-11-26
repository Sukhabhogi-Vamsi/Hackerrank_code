def plusMinus(arr):
    pos = []
    neg = []
    zero = []
    n=len(arr)
    for i in range(n):
        if arr[i]>0:
            pos.append(arr[i])
        elif arr[i]<0:
            neg.append(arr[i])
        elif arr[i] == 0:
            zero.append(arr[i])
    pos1 = len(pos)/n
    neg1 = len(neg)/n
    zero1 = len(zero)/n
    print('{:.6f}'.format(pos1))
    print('{:.6f}'.format(neg1))
    print('{:.6f}'.format(zero1))

arr = [-4, 3, -9, 0, 4, 1]
op = plusMinus(arr)