from functions import Calculator
from operations import Inputer

# 1 СТВОРЕННЯ ОБ'ЄКТІВ
my_calc = Calculator()
my_input = Inputer()

# 2 ОТРИМАННЯ ДАНИХ
num1 = my_input.get_number()
operator = my_input.get_operator()
num2 = my_input.get_number()

# 3 ОБЧИСЛЕННЯ
if operator == "+":
    result = my_calc.add(num1, num2)
elif operator == "-":
    result = my_calc.sub(num1, num2)
elif operator == "*":
    result = my_calc.mul(num1, num2)
elif operator == "/":
    result = my_calc.div(num1, num2)
else:
    result = "Невідома операція"

# 4 РЕЗУЛЬТАТ
print(f"Результат: {result}")