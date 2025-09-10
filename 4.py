name = input("Введите имя: ")
surname = input("Введите фамилию: ")
ot = input("Введите отчество (Нажите Enter, если нет): ")

num = int(input("Введите число для размена: "))


mon1 = len(name)
mon2 = len(surname)
mon3 = len(ot) if len(ot) > 0 else 19

# k1, k2, k3 = 0, 0, 0
#
# monets = sorted([[mon1, 0], [mon2, 0], [mon3, 0]])
# print(monets)
# while num > 0:
#     if num >= monets[2][0]:
#         num -= monets[2][0]
#         monets[2][1] += 1
#
#     elif num >= monets[1][0]:
#         num -= monets[1][0]
#         monets[1][1] += 1
#
#     elif num >= monets[0][0]:
#         num -= monets[0][0]
#         monets[0][1] += 1
#
#     else:
#         break
#
#
# for i, j in monets:
#     if j != 0:
#         print(f"Требуется {j} монет {i}", end=" ")
#
#
res = [[0, 0, 0] for _ in range(num + 1)]
coins = [mon1, mon2, mon3]


for i in range(1, num + 1):
    for coin in coins:
        if i - coin >= 0:
            if res[i - coin][0] != 0 or i - coin == 0:
                res[i][0] = res[i - coin][0] + 1
                res[i][1] = coin
                res[i][2] = i - coin




def back():
    listt = []
    i = -1
    while i != 0:
        steps, coin, before = res[i]
        listt.append(coin)
        i = before
        if steps == 1:
            break

    return listt


needed = res[-1][0]
if needed > 0:
    listt = back()
    print(listt)
    print("Размен:")
    count_m1 = listt.count(mon1)
    count_m2 = listt.count(mon2)
    count_m3 = listt.count(mon3)
    if count_m1 != 0:
        print(listt.count(mon1), "по", mon1)
    if count_m2 != 0:
        print(listt.count(mon2), "по", mon2)
    if count_m3 != 0:
        print(listt.count(mon3), "по", mon3)

else:
    print("-42!")
