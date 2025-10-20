def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def dil(a, b):
    # Обробка ділення на нуль
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе!")
    return a / b

while True:
    dia = input("Привіт, виберіть дію серед запропонованих:  + - * /  або 'q' для виходу: ")
    if dia == "q":
        print("До побачення!")
        break

    try:
        # Перевірка правильності введення чисел
        a = int(input("Перше число: "))
        b = int(input("Друге число: "))
    except ValueError:
        print("Будь ласка, вводьте лише цілі числа!")
        continue

    try:
        match dia:
            case "+":
                print(plus(a, b))
            case "-":
                print(minus(a, b))
            case "*":
                print(multi(a, b))
            case "/":
                print(dil(a, b))
            case _:
                print("Неправильна дія")
    except ZeroDivisionError as e:
        print(e)