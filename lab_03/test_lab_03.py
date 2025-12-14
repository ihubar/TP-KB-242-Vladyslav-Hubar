import pytest
from student import Student
from StudentList import StudentList

def test_add_student():
    sl = StudentList()
    s1 = Student("Bob", "123", "email", "group")
    
    sl.add_student(s1)
    
    assert len(sl.students) == 1
    assert sl.students[0].name == "Bob"

def test_delete_student():
    sl = StudentList()
    s1 = Student("Bob", "123", "email", "group")
    sl.add_student(s1)
    
    result = sl.delete_student("Bob")
    
    assert result is True
    assert len(sl.students) == 0

def test_update_student():
    sl = StudentList()
    s1 = Student("Bob", "111", "email", "group")
    sl.add_student(s1)
    
    s2 = Student("Bob", "222", "new_email", "new_group")
    
    result = sl.update_student("Bob", s2)
    
    assert result is True
    assert sl.students[0].phone == "222"