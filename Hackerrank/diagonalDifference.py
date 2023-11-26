def diagonalDifference(arr):
    n = len(arr)
    ltr, rtl = 0, 0
    for i in range(n):
        ltr += arr[i][i]
        rtl += arr[i][n-i-1]
    return abs(ltr-rtl)
arr = [[11,2,4], [4, 5, 6], [10,8,-12]]
diagonal_diff = diagonalDifference(arr)
print("Diagonal difference:", diagonal_diff)