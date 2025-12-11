# 1 клас
class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

# 2 список студентів
students = [
    Student("Олег", 21),
    Student("Анна", 19),
    Student("Богдан", 20),
    Student("Марія", 18)
]

for s in students:
    print(s)

# 3 Сортування
sorted_students = sorted(students, key=lambda x: x.age)

print("\n--- Після сортування (від наймолодшого) ---")
for s in sorted_students:
    print(s)