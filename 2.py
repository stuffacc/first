import sys
from functools import lru_cache

sys.set_int_max_str_digits(10 ** 6)


n_str = input("Введите фамилию: ")

n = len(n_str)


@lru_cache(maxsize=5)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10 ** 6 + n + 1):
    fibonacci(i)

fib = fibonacci(10 ** 6 + n)

print(fib % 239)
