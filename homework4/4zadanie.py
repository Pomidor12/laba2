def find_multiples(x, numbers):
    is_multiple = lambda num: num % x == 0
    multiples = list(filter(is_multiple, numbers))
    return multiples

if __name__ == "__main__":
    x = int(input("Введите число X: "))
    numbers = random.sample(range(201), 10) 
    print(f"Случайный список чисел: {numbers}")
    multiples = find_multiples(x, numbers)
    print(f"Числа, кратные {x}: {multiples}")