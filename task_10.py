coin_count = int(input("Введите число монет: "))
print("Количество монет:", coin_count)
coins = []
flips = 0
for i in range(0, coin_count):
    coins.append(int(input(f"Задайте положение монеты {i}: ")))
for i in range(0, coin_count):
    if coins[i] == 0:
        flips += 1
print(f"Необходимо перевернуть минимум {flips} монет")
