# Given array and target value
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
x = 13
n = len(array)


# initialize k and b
k = 0
b = n // 2

while b >= 1:
    while k + b < n and array[k + b] <= x:
        k += b
    b //= 2

if array[k] == x:
    print(f"x found at index {k}")


