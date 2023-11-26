string = 'my name is vamsi'
print(string)
my_set = set(string)
for i in my_set:
    count = 0
    for j in string:
        if j==i:
            count+=1
    print(f'character {i} is {count} times occured')