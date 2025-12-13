import csv
import sys

student_list = []

def add_student(name, phone, email, group):
    new_item = {"name": name, "phone": phone, "email": email, "group": group}
    insert_pos = 0
    for item in student_list:
        if name > item["name"]:
            insert_pos += 1
        else:
            break
    student_list.insert(insert_pos, new_item)
    return new_item

def delete_student(name):
    for item in student_list:
        if name == item["name"]:
            student_list.remove(item)
            return True
    return False

def update_student(name, field, new_value):
    for item in student_list:
        if name == item["name"]:
            item[field] = new_value
            return True
    return False

# --- Робота з файлами та Меню ---

def load_from_csv(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student_list.append(row)
        print("Дані завантажено.")
    except FileNotFoundError:
        print("Файл не знайдено, список порожній.")

def save_to_csv(filename):
    with open(filename, "w", encoding="utf-8", newline='') as f:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_list)
    print("Дані збережено.")

def main():
    if len(sys.argv) < 2:
        return
    
    csv_file = sys.argv[1]
    load_from_csv(csv_file)

    while True:
        choice = input("\nДія [C create, U update, D delete, P print, X exit]: ")
        
        if choice.lower() == "c":
            print("Додавання:")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            group = input("Group: ")
            add_student(name, phone, email, group)
            print("Додано.")

        elif choice.lower() == "d":
            name = input("Ім'я для видалення: ")
            if delete_student(name):
                print("Видалено.")
            else:
                print("Не знайдено.")

        elif choice.lower() == "u":
            name = input("Ім'я для оновлення: ")
            field = input("Що змінити (phone/email/group): ")
            val = input("Нове значення: ")
            if update_student(name, field, val):
                print("Оновлено.")
            else:
                print("Помилка.")

        elif choice.lower() == "p":
            for s in student_list:
                print(s)

        elif choice.lower() == "x":
            save_to_csv(csv_file)
            break

if __name__ == "__main__":
    main()