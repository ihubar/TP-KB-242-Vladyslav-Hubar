import requests  

# 1 Запитуємо у користувача дані
currency_code = input("Введіть валюту (USD, EUR, PLN): ").strip().upper()
amount = float(input("Введіть суму валюти: "))

# 2 Отримуємо офіційні курси від НБУ
response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
data = response.json()  # Перетворюємо відповідь у зручний список

# 3 Шукаємо потрібну валюту у списку
found = False
for item in data:
    if item['cc'] == currency_code:
        # Знайшли! Рахуємо результат
        rate = item['rate']
        result = amount * rate
        print("Курс:",currency_code,rate)
        print("Результат:",result,"грн")
        found = True
        break  # Зупиняємо пошук

if not found:
    print("Таку валюту не знайдено або введено неправильно.")