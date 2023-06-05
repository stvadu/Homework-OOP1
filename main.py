import sys
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_grades = 0
        len_grades = 0
        for all_grades in self.grades.values():
            for course_grades in all_grades:
                len_grades += 1
                sum_grades += course_grades
            avg = sum_grades / len_grades
        return avg

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {self.average_grade()}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, student):
        return self.average_grade() < student.average_grade()

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
        sum_grades = 0
        len_grades = 0
        for all_grades in self.grades.values():
            for course_grades in all_grades:
                len_grades += 1
                sum_grades += course_grades
            avg = sum_grades / len_grades
        return avg

    def __lt__(self, lecturer):
       return self.average_grade() < lecturer.average_grade()
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

def average_grade_hm(students_list,course):
    avg_all_students_hm = []
    for student in students_list:
        avg_student_hm = sum(student.grades.get(course))/len(student.grades.get(course))
        avg_all_students_hm.append(avg_student_hm)
    avg_hm = sum(avg_all_students_hm)/len(avg_all_students_hm)
    return avg_hm

def average_grade_lec(lecturers_list,course):
    avg_all_lecturers = []
    for lecturer in lecturers_list:
        avg_lecturers = sum(lecturer.grades.get(course))/len(lecturer.grades.get(course))
        avg_all_lecturers.append(avg_lecturers)
    avg_lec = sum(avg_all_lecturers)/len(avg_all_lecturers)
    return avg_lec

Student1 = Student('Ivan', 'Ivanov', 'male')
Student1.courses_in_progress = ['Python']
Student1.finished_courses = ['Git', 'C++']
Student1.grades = {'Git': [8, 6, 6], 'C++': [9, 10, 9]}

Student2 = Student('Petr', 'Petrov', 'male')
Student2.courses_in_progress = ['C++']
Student2.finished_courses = ['Git', 'Python']
Student2.grades = {'Git': [10, 7, 7], 'Python': [7, 9, 4, 5]}

Reviewer1 = Reviewer('Marya', 'Kotova')
Reviewer1.courses_attached = ['Git']

Reviewer2 = Reviewer('Sergey', 'Petukhov')
Reviewer2.courses_attached = ['Python', 'C++']

Lecturer1 = Lecturer('Inna', 'Vanina')
Lecturer1.courses_attached = ['Python', 'Git']
Lecturer1.grades = {'Python': [8, 6]}

Lecturer2 = Lecturer('Oleg', 'Bekov')
Lecturer2.courses_attached = ['Python', 'C++']
Lecturer2.grades = {'Python': [10, 8]}

print('Студенты:')
print(Student1)
print(Student2)
print('Ревьюеры:')
print(Reviewer1)
print(Reviewer2)
print('Лекторы:')
print(Lecturer1)
print(Lecturer2)
print(Student1.surname, 'успешнее', Student2.surname, '?')
print(Student1 > Student2)
print(Lecturer1.surname, 'лучше объясняет, чем', Lecturer2.surname, '?')
print(Lecturer1 > Lecturer2)
print('Средняя оценка за ДЗ:')
print(average_grade_hm([Student1, Student2], 'Git'))
print('Средняя оценка за лекции:')
print(average_grade_lec([Lecturer1, Lecturer2], 'Python'))