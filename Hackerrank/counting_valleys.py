def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    count = 0
    for i in path:
        if i == "U":
            sea_level += 1
            if sea_level == 0:
                count += 1
        elif i == "D":
            sea_level -= 1
    return count
print(countingValleys(steps=8,path=[DDUUUUDD]))