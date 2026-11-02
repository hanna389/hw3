import random

result1 = random.random()
print("Функція random.random() повертає число float від 0.0 до 1.0 (не включно):", result1)

result2 = random.randint(1, 10)
print("Функція random.randint(a, b) повертає число int від a до b (включно):", result2)

elements = ["laptop", 2, True, 4, "apple", False]
result3 = random.choice(elements)
print("Функція random.choice() повертає будь-який елемент з непорожньої послідовності:", result3)
