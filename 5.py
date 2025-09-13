s1 = input("Введите первую строку: ").lower()
s2 = input("Введите вторую строку: ").lower()

def f(s1, s2):
    return [s1, s2] == sorted([s1, s2], reverse=True)


print("Строки в обратном лексикографическом порядке:", f(s1, s2))
