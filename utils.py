import json

def load_studentns():
    with open('student.json') as file:
        students = json.load(file)
        return students


def load_professions():
    with open("professions.json") as file:
        professions = json.load(file)
    return professions


def get_student_by_pk():
    for stude in student:
        if pk is stude['pk']:
            print(f"Студент: {stude['full_name']}\nЗнает: {', '.join(stude['skills'])}")
            student_skill = set(stude['skills'])
            return student_skill
    else:
        print("Такого студента нет")
        quit()


def get_professions_by_title():
    for prof in profession:
        if title in prof['title']:
            prof_skills = set(prof['skills'])
            return prof_skills
    else:
        print("В списке нет такой профессии")
        quit()


def check_fitness(student_skill, prof_skills):
    intersect = student_skill.intersection(prof_skills)
    differ_skill = prof_skills.difference(student_skill)
    procent = 100 // len(prof_skills) * len(intersect)
    print(f"Профпригодность = {procent} %")
    print(f"Для профессии знает: {', '.join(intersect)}")
    print(f"Для профессии не знает: {', '.join(differ_skill)}")


if __name__ == "__main__":
    student_skill = set()
    prof_skills = set()
    student = load_studentns()
    profession = load_professions()
    pk = int(input("Введите номер студента\n"))
    get_student_by_pk()
    title = input("Введите специальность для оценки\n")
    check_fitness(get_student_by_pk(), get_professions_by_title())

