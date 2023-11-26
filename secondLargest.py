def print2large(arr):
    s = set(arr)
    if len(s)==1:
        return -1
    else:
        op = sorted(set(s))
        print(op[-2])
#arr=[642,642,642,642,642,642,642,642,642,642,642,642,642,642,642,642,642,642,642,642,642]
arr=[12,35,1,10,34,1]
print(print2large(arr))