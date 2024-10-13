import random

def get_user_choice():
    while True:
        user_choice = input("Выберите камень, ножницы или бумагу: ").lower()
        if user_choice in ["камень", "ножницы", "бумага"]:
            return user_choice
        else:
            print("Неверный выбор. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")

def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
        (user_choice == "ножницы" and computer_choice == "бумага") or \
        (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы победили!"
    else:
        return "Компьютер победил!"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print(winner)

    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again != "да":
        break

print("Спасибо за игру!")