def countApplesAndOranges(s, t, a, b, apples, oranges):
    res1 = []
    res2 = []
    cnt1 = 0
    cnt2 = 0
    for i in apples:
        res1.append(i+a)
    for j in oranges:
        res2.append(j+b)
    for k in res1:
        if k >= s and k <= t:
            cnt1 += 1
    for l in res2:
        if l >= s and l <= t:
            cnt2 += 1
    print(cnt1)
    print(cnt2)
s = 7
t = 10
a = 4
b = 12
countApplesAndOranges(s,t,a,b,apples=[2,3,-4],oranges=[3,-2,-4])