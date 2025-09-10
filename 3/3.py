arr = [i for i in range(2, 10**5)]


def div(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


for i in range(len(arr)):
    curr = arr[i]
    if curr != 0 and div(curr):
        for j in range(i + curr, len(arr), curr):
            arr[j] = 0

arr = [i for i in arr if i != 0]
print(arr)
