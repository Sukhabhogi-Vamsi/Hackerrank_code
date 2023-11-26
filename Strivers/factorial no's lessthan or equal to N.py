def factorialNumbers(n):
    res=1
    cnt=1
    ans=[]
    while res <= n:
        res= res*cnt
        if res<=n:
            ans.append(res)
            cnt+=1
    return ans
print(factorialNumbers(7))