def find_multiples(x, numbers):
    """
    Ищет числа, кратные заданному числу X, в списке чисел.

    Args:
        x: Число, кратные которому нужно найти.
        numbers: Список чисел для поиска.

    Returns:
        Список чисел, кратных X.
    """

    is_multiple = lambda num: num % x == 0
    multiples = list(filter(is_multiple, numbers))
    return multiples

if __name__ == "__main__":
    x = int(input("Введите число X: "))
    numbers = random.sample(range(201), 10)  # Генерируем случайный список из 10 чисел от 0 до 200
    print(f"Случайный список чисел: {numbers}")
    multiples = find_multiples(x, numbers)
    print(f"Числа, кратные {x}: {multiples}")