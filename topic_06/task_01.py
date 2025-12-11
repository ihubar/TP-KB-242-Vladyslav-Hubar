import functions
import operations

print("--- Калькулятор з логуванням ---")

# 1. Питаємо числа та дію
num1 = operations.ask_number()
operator = operations.ask_operator()
num2 = operations.ask_number()

# 2. Рахуємо результат
result = None
if operator == "+":
    result = functions.add(num1, num2)
elif operator == "-":
    result = functions.sub(num1, num2)
elif operator == "*":
    result = functions.mul(num1, num2)
elif operator == "/":
    result = functions.div(num1, num2)
else:
    result = "Помилка"

# 3. Виводимо на екран
print("Результат:", result)

# 4. ЛОГУВАННЯ
log_text = f"{num1} {operator} {num2} = {result}"
with open("history.txt", "a") as file:
    file.write(log_text + "\n")