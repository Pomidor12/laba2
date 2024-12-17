def get_number():
    """Генератор, возвращающий нечётные числа из диапазона 0-30."""
    for number in range(30):
        if number % 2 != 0:  # Проверяем, является ли число нечетным
            yield number

def main():
    # Создаем генератор
    odd_numbers = get_number()
    
    # Сохраняем значения в список для последующего доступа
    odd_numbers_list = list(odd_numbers)

    # Проверяем, достаточно ли нечётных чисел в списке
    if len(odd_numbers_list) >= 5:
        # Выводим первое, пятое и последнее значения
        print(f"Первое нечётное число: {odd_numbers_list[0]}")
        print(f"Пятое нечётное число: {odd_numbers_list[4]}")
        print(f"Последнее нечётное число: {odd_numbers_list[-1]}")
    else:
        print("Недостаточно нечётных чисел в диапазоне.")

if __name__ == "__main__":
    main()
