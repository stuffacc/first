s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")

alf = "0123456789abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def func(s1, s2):
    t1 = s1.lower()
    t2 = s2.lower()
    if len(t1) > len(t2):
        return [s1, s2]
    elif len(t1) < len(t2):
        return [s2, s1]
    else:
        for i in range(len(t1)):
            cur1 = t1[i]
            cur2 = t2[i]
            if cur1 == cur2:
                continue
            elif alf.find(cur1) > alf.find(cur2):
                return [s1, s2]
            else:
                return [s2, s1]

        return [s1, s2]

if "ё" in s1.lower() or "ё" in s2.lower():
    print(func(s1, s2))
else:
    sorted([s1, s2], reverse=True)

