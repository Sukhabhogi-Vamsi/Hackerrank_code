def camelcase(s):
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count
print(camelcase(s=input("Enter a string: ")))