
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@example.com", "group":"KB-291"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@example.com", "group":"KB-291"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@example.com", "group":"KB-292"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@example.com", "group":"KB-292"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Email is  " + elem["email"] + ", group is  " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email:")
    group = input("Please enter student group:")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    
    #Знайти студента
    findPosition = -1

    for item in list:
        if name == item["name"]:
            findPosition = list.index(item)
            break
        
    #Якщо не знайдено
    if findPosition == -1:
        print("Student not found")
        return
    
    #Показати поточні дані
    print("Current data:", list[findPosition])
    
    #Запитати що саме змінити
    print("What do you want to update?")
    print("1 - Name")
    print("2 - Phone")
    print("3 - Email")
    print("4 - Group")
    choice = input("Enter choice: ")
    
    if choice == "1":
        new_name = input("Enter new name: ")
        
        # Зберегти всі дані студента
        old_data = list[findPosition]
        
        # Видалити старий запис
        del list[findPosition]
        
        # Створити новий запис з новим іменем
        newItem = {
            "name": new_name, 
            "phone": old_data["phone"],
            "email": old_data["email"],
            "group": old_data["group"]
        }
        
        # Знайти правильну позицію для нового імені
        insertPosition = 0
        for item in list:
            if new_name > item["name"]:
                insertPosition += 1
            else:
                break
        
        # Вставити на правильну позицію
        list.insert(insertPosition, newItem)
        print("Name updated and list sorted")
        
    elif choice == "2":
        new_phone = input("Enter new phone: ")
        list[findPosition]["phone"] = new_phone
        print("Phone updated")
        
    elif choice == "3":
        new_email = input("Enter new email: ")
        list[findPosition]["email"] = new_email
        print("Email updated")
        
    elif choice == "4":
        new_group = input("Enter new group: ")
        list[findPosition]["group"] = new_group
        print("Group updated")
    
    else:
        print("Invalid choice")


def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()