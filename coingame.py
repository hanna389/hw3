import random


counts = {}
options = ["Аверс", "Реверс"]

coin_toss = random.randint(100, 1000)
print("Кількість кидків: ", coin_toss)

for _ in range(coin_toss):
    value = random.choice(options)
    if value not in counts:
        counts[value] = 0
    counts[value] +=1

print(counts)