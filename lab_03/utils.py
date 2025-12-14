import csv
from student import Student

class FileReader:
    def save_to_csv(self, filename, student_list):
        with open(filename, "w", encoding="utf-8", newline='') as file:
            fieldnames = ["name", "phone", "email", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list:
                writer.writerow({
                    "name": student.name,
                    "phone": student.phone,
                    "email": student.email,
                    "group": student.group
                })
        print("Дані збережено")

    def load_from_csv(self, filename):
        students = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    obj = Student(row["name"], row["phone"], row["email"], row["group"])
                    students.append(obj)
            print("Дані завантажено")
        except FileNotFoundError:
            print("Файл не знайдено")
        return students