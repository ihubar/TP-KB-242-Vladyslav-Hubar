my_list = [1, 2, 3]
print("Початковий список:", my_list)

# append() - додає один елемент в кінець списку
my_list.append(4)
print("Після append(4):", my_list)

# extend() - додає кілька елементів з іншого списку
my_list.extend([5, 6])
print("Після extend([5, 6]):", my_list)

# insert(index, val) - вставляє елемент на позицію
my_list.insert(2,10)
print("Після insert(2,10):", my_list)

# reverse() - перевертає список
my_list.reverse()
print("Після reverse():", my_list)

# remove(val) - видаляє перший елемент з таким значенням
my_list.remove(5)
print("Після remove(5):", my_list)

# sort() - сортує список
my_list.sort()
print("Після sort():", my_list)

# copy() - створює копію списку
my_list_copy = my_list.copy()
print("Після copy():")
print("Оригінал:", my_list)
print("Копія:", my_list_copy)

# clear() - очищує весь список
my_list.clear()
print("Після clear():", my_list)