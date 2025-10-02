def find_position(my_list, element):
    for i in range(len(my_list)):
        if element < my_list[i]:
            return i
    return len(my_list)

my_list = [1, 4, 6, 7, 10]
print("Відсортований список: ", my_list)
element = int(input("Виберіть число для вставки в список: "))

pos = find_position(my_list, element)
print("Позиція для вставки: ", pos)


my_list.insert(pos, element)
print("Список після вставки: ", my_list)