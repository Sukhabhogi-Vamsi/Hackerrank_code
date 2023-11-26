import math
def viralAdvertising(n):
    shared = 5
    liked = math.floor(shared/2)
    cumulative = 2
    for day in range(2, n+1):
        shared = liked * 3
        liked = math.floor(shared / 2)
        cumulative += math.floor(shared/2)
    return cumulative
print(viralAdvertising(5))