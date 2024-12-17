from datetime import date, datetime

def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y").date()
    except ValueError:
        raise ValueError("Неверный формат даты рождения. Используйте формат день.месяц.год (например 03.09.2014)")

    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

while __name__ == "__main__":
    print('Для выхода из программы введите "q"')
    birthdate = input("Введите дату рождения в формате день.месяц.год (например 03.09.2014): ")
    if birthdate == "q":
        break
    try:
        age = calculate_age(birthdate)
        print(f"Ваш возраст: {age} лет")
    except ValueError as e:
        print(e)
