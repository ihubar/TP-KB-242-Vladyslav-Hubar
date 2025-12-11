class Phone:
    # __init__ запускається при створенні телефону
    def __init__(self, model, price):
        self.model = model
        self.price = price

    # __str__ запускається, коли робимо print(phone)
    def __str__(self):
        return f"Телефон: {self.model}, Ціна: {self.price}$"

# Використання:
iphone = Phone("iPhone 15", 1000)  # Спрацював __init__
samsung = Phone("Galaxy S24", 950) # Спрацював __init__

print(iphone)   
print(samsung)  