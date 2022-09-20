import json
import re


def load_students(filepath: str) -> list:
    """
    Загружает базу студентов
    """
    with open(filepath) as file:
        students_data = json.load(file)
        return students_data


def get_student_data_by_pk(students_data: list, pk: int) -> dict or None:
    """
    Получает вданные студента по ключу
    """
    for student in students_data:
        if pk == student['pk']:
            print(f"Студент: {student['full_name']}")
            return student
    else:
        print("Такого студента нет")
        return None


def get_pk_from_user() -> int or quit:
    """
    Получаем корректный ключ от пользователя
    """
    while True:
        pk = input("Введите номер студента\n")
        if pk.isdigit():
            pk = int(pk)
            return pk
        elif pk == "stop":
            print("приходи ещё")
            quit()


def is_valid_login(student: dict) -> bool:
    """
    Проверяем логин на соответствие требованиям
    """
    student_login = student['login']
    regex = r"(?=^[^A-Z])(?=.*\d)(?=.*[!@#$%:\"?,.*\[\]{}()&\\\-_+=<>;'|~&])(?=.*[\da-zA-Z]$).{4,}"
    if re.search(regex, student_login):
        return True
    return False


def main() -> None:
    students_data = load_students('student.json')
    while True:
        pk = get_pk_from_user()
        student = get_student_data_by_pk(students_data, pk)

        if student is None:
            continue

        elif is_valid_login(student):
            print("Логин класс")

        else:
            print("Увы перезапиши")


if __name__ == "__main__":
    main()
