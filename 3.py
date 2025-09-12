# Решето Эратосфена 2.0

arr = [True for _ in range(0, 10 ** 7)]
arr[0], arr[1] = False, False

for i in range(len(arr)):
    if arr[i]:
        for j in range(i**2, len(arr), i):
            arr[j] = False

arr = [i for i in range(len(arr)) if arr[i]]
print(arr)
