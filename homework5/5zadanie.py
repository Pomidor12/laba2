def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

numbers = get_number()
print("Первое число:", next(numbers))
for _ in range(4):
    next(numbers)
print("Пятое число:", next(numbers))
for _ in numbers:
    pass
print("Последнее число:", next(numbers))