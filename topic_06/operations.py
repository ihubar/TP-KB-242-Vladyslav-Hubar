# Функції для введення даних
def ask_number():
    text = input("Введіть число: ")
    return float(text)

def ask_operator():
    op = input("Введіть дію (+, -, *, /): ")
    return op