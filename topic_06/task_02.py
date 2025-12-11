students = [
    {'name': 'Max', 'grade': 85},
    {'name': 'Dima', 'grade': 92},
    {'name': 'Stas', 'grade': 60}
]

# x - це один студент зі списку. x['grade'] - це його оцінка
sorted_students = sorted(students, key=lambda x: x['grade']) 

for student in sorted_students:
    print(f"Name: {student['name']}, Grade: {student['grade']}")