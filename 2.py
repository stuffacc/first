n_str = input("Введите фамилию: ")
n = len(n_str)

oldest = 0
older = 1
for i in range(2, 10**6 + n):
    older, oldest = oldest + older, older


print(older % 239)
