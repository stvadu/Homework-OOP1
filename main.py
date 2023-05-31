class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = dict()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if len(self.grades) > 0:
           avg = sum(self.grades.values()) / len(self.grades)
        else: avg = 'нет оценок'
        return avg

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {self.average_grade()}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, student):
        return self.average_grade() > student.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.average_grade()}\n'

    def average_grade(self):
        if len(self.grades) > 0:
            avg = sum(self.grades) / len(self.grades)
        else: avg = 'нет оценок'
        return avg

    def __lt__(self, lecturer):
       return self.average_grade() > lecturer.average_grade()
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'

Student1 = Student('Ivan', 'Ivanov', 'male')
Student1.courses_in_progress = ['Python', 'Git']
Student1.finished_courses = ['C++']
Student1.grades = {1 : 9}

Student2 = Student('Petr', 'Petrov', 'male')
Student2.courses_in_progress = ['C++']
Student2.finished_courses = ['Git', 'Python']
Student2.grades = {1 : 7, 2 : 8}

Reviewer1 = Reviewer('Marya', 'Kotova')
Reviewer1.courses_attached = ['Git']

Reviewer2 = Reviewer('Sergey', 'Petukhov')
Reviewer2.courses_attached = ['Python', 'C++']

Lecturer1 = Lecturer('Inna', 'Vanina')
Lecturer1.courses_attached = ['Git']
Lecturer1.grades = {5}

Lecturer2 = Lecturer('Oleg', 'Bekov')
Lecturer2.courses_attached = ['Python', 'C++']
Lecturer2.grades = {10, 9}

print('Студенты:')
print(Student1)
print(Student2)
print('Ревьюеры:')
print(Reviewer1)
print(Reviewer2)
print('Лекторы:')
print(Lecturer1)
print(Lecturer2)
print(Student1 > Student2)
print(Lecturer1 > Lecturer2)
