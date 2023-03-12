coin_count = int(input("Введите число монет: "))
print("Количество монет:", coin_count)
coins = []
tails = 0
eagles = 0
for i in range(0, coin_count):
    coins.append(int(input(f"Задайте положение монеты {i}: ")))
for i in range(0, coin_count):
    if coins[i] == 0:
        tails +=1
    else: eagles +=1
if tails >= eagles:
    print(f"Необходимо перевернуть минимум {eagles} монет")
else:
    print(f"Необходимо перевернуть минимум {tails} монет")