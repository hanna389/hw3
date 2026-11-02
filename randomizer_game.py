import random


options = ["камінь", "ножиці", "папір"]

while True:
    try:
        player_choice = input(f"Введіть свій вибір: {options}").strip().lower()

        if player_choice not in options:
            raise ValueError("Цього варіанта немає у списку.") 

    except ValueError as error:
        print(f"Помилка: {error} Спробуйте знову.\n")
        continue

    computer_choice = random.choice(options)
    print(f"Ваш хід: {player_choice}; Хід комп'ютера: {computer_choice}")

    if player_choice == computer_choice:
        print("Нічия!\n")
    elif (
      (player_choice == "камінь" and computer_choice == "ножиці")
      or (player_choice == "ножиці" and computer_choice == "папір")
      or (player_choice == "папір" and computer_choice == "камінь")
  ):

        print("Ви виграли!")
    else:
        print("Комп'ютер виграв!")
    break

