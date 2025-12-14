class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        insert_pos = 0
        for item in self.students:
            if student.name > item.name:
                insert_pos += 1
            else:
                break
        self.students.insert(insert_pos, student)

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def update_student(self, name, new_student):
        if self.delete_student(name):
            self.add_student(new_student)
            return True
        return False

    def get_all(self):
        return self.students