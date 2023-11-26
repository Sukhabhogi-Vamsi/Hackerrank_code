import math

def gradingStudents(grades):
    lst = []
    for i in grades:
        g =((math.floor(i/5)) *5) + 5
        if i < 38:
            lst.append(i)
        elif (g-i)>=3:
            lst.append(i)
        elif (g-i) < 3:
            lst.append(g)
    return lst

grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
grades.append(grades_item)
result = gradingStudents(grades)