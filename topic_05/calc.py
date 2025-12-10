import functions
import operations

print("--- Простий Калькулятор ---")

# 1. Просимо ввести дані (використовуємо файл operations)
num1 = operations.ask_number()
operator = operations.ask_operator()
num2 = operations.ask_number()

# 2. Перевіряємо дію і рахуємо (використовуємо файл functions)
if operator == "+":
    result = functions.add(num1, num2)
elif operator == "-":
    result = functions.sub(num1, num2)
elif operator == "*":
    result = functions.mul(num1, num2)
elif operator == "/":
    result = functions.div(num1, num2)
else:
    result = "Невідома дія"

# 3. Виводимо результат
print("Відповідь:",result)