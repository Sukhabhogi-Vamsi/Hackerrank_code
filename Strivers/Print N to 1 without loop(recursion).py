l = list()
def func(x):
    if x<1:
        return
    else:
        l.append(x)
        func(x - 1)
    return l
print(func(5))