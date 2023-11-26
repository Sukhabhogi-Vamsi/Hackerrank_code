def kangaroo(x1,v1,x2,v2):
    for i in range(10000):
        if x1+i*v1 == x2+i*v2:
            return "YES"
    return "NO"
print(kangaroo(0,4,3,2))