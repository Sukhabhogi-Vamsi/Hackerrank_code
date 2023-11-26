def utopianTree(n):
    height = 1
    for i in range(1,n+1):
        if i % 2 == 1:
            height *= 2
        elif i % 2 == 0:
            height += 1
    return height
print(utopianTree(5))