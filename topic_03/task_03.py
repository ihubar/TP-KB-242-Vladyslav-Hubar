my_dict = {"a": 1, "b": 2, "c": 3}
print("Початковий словник:", my_dict)

my_dict.update({"d":4})
print("Оновлений словник: ", my_dict)

del my_dict["d"]
print("Словник після видалення ключа:", my_dict)

print("Ключі:", my_dict.keys())

print("Значення:", my_dict.values())

print("Ключ + значення:", my_dict.items())