import pytest
import lab_02

# Ця функція очищує список перед кожним тестом, щоб тести не заважали один одному.
@pytest.fixture(autouse=True)
def clear_list():
    lab_02.student_list = []

def test_add_student():
    # Викликаємо функцію напряму, передаючи дані
    lab_02.add_student("Bob", "1234567890", "bob@email.com", "CS-1")
    
    # Перевіряємо результат у списку
    assert len(lab_02.student_list) == 1
    assert lab_02.student_list[0]["name"] == "Bob"
    assert lab_02.student_list[0]["phone"] == "1234567890"

def test_delete_student():
    #Перевірка видалення студента
    lab_02.add_student("Bob", "123", "email", "group")
    assert len(lab_02.student_list) == 1
    
    # Видаляємо
    result = lab_02.delete_student("Bob")
    
    # Перевіряємо, що функція повернула True і список порожній
    assert result is True
    assert len(lab_02.student_list) == 0

def test_delete_student_not_found():
    #Перевірка видалення неіснуючого студента
    lab_02.add_student("Bob", "123", "email", "group")
    
    # Пробуємо видалити того, кого немає
    result = lab_02.delete_student("Alice")
    
    # Перевіряємо, що функція повернула False, а Боб залишився
    assert result is False
    assert len(lab_02.student_list) == 1

def test_update_student():
    #Перевірка оновлення даних
    lab_02.add_student("Bob", "111", "email", "group")
    
    # Оновлюємо телефон
    result = lab_02.update_student("Bob", "phone", "999")
    
    assert result is True
    assert lab_02.student_list[0]["phone"] == "999"

def test_update_student_not_found():
    #Перевірка оновлення неіснуючого студента
    result = lab_02.update_student("Alice", "phone", "999")
    assert result is False