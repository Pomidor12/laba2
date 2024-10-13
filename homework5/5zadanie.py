def get_number():
    """Генератор нечетных чисел из диапазона range(30)."""
    for num in range(30):
        if num % 2 != 0:
            yield num

# Создаем генератор
numbers = get_number()

# Выводим первое, пятое и последнее значение
print("Первое число:", next(numbers))

for _ in range(4): # Пропускаем следующие 4 значения
    next(numbers)

print("Пятое число:", next(numbers))

for _ in numbers: # Пропускаем все остальные значения до последнего
    pass

print("Последнее число:", next(numbers))