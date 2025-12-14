import sys
from student import Student
from StudentList import StudentList
from utils import FileReader

def main():
    if len(sys.argv) < 2:
        return
    
    file_name = sys.argv[1]
    
    my_list = StudentList()
    file_helper = FileReader() 
    
    loaded_students = file_helper.load_from_csv(file_name)
    for s in loaded_students:
        my_list.students.append(s)

    while True:
        choice = input("\nДія [C create, U update, D delete, P print, X exit]: ")
        
        if choice.lower() == "c":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            group = input("Group: ")
            new_student = Student(name, phone, email, group)
            my_list.add_student(new_student)
            print("Додано.")

        elif choice.lower() == "d":
            name = input("Ім'я для видалення: ")
            if my_list.delete_student(name):
                print("Видалено.")
            else:
                print("Не знайдено.")

        elif choice.lower() == "u":
            name = input("Ім'я для оновлення: ")
            print("Введіть нові дані:")
            new_n = input("New Name: ")
            new_p = input("New Phone: ")
            new_e = input("New Email: ")
            new_g = input("New Group: ")
            new_obj = Student(new_n, new_p, new_e, new_g)
            
            if my_list.update_student(name, new_obj):
                print("Оновлено")
            else:
                print("Не знайдено")

        elif choice.lower() == "p":
            for s in my_list.get_all():
                print(s)

        elif choice.lower() == "x":
            file_helper.save_to_csv(file_name, my_list.get_all())
            break

if __name__ == "__main__":
    main()