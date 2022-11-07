def average(list):
    s = 0
    c = 0
    for i in list.values():  # считаем среднее арифметическое оценок по всем курсам
        for j in i:
            s += int(j)
            c += 1
    s = s / c
    return s


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # здесь определяем функцию, которая выставляет оценки Lecturer
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
             f'Фамилия: {self.surname}\n' \
             f'Средняя оценка за домашние задания: {round(average(self.grades), 2)}\n' \
             f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
             f'Завершенные курсы: {", ".join(self.finished_courses)}  \n'
        return res

    def __lt__(self, other):  # сравниваем студентов по средним оценкам
        if not isinstance(other, Student):
            print('Not a student!')
            return
        return average(self.grades) < average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
   
    # надо определить здесь словарь, в котором хранятся оценки для Lecturer
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {round(average(self.grades), 2)} \n'
        return res

    def __lt__(self, other):  # сравниваем лекторов по средней оценке
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return average(self.grades) < average(other.grades)


class Reviewer(Mentor):
    
    # Пишем функцию выставления оценок только Reviewer
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n'
        return res


some_reviewer = Reviewer('Adrian', 'Paul')
print(some_reviewer)

student_one = Student('Germiona', 'Granger', 'femail')
student_one.finished_courses += ['Git']
student_one.courses_in_progress += ['Python', 'Pascal']
student_one.add_courses('OOP')
student_one.grades['Git'] = [10, 20, 30, 40, 10]
student_one.grades['Python'] = [30, 30]
print(student_one)

student_two = Student('Boby', 'Fisher', 'male')
student_two.finished_courses += ['Git']
student_two.courses_in_progress += ['Python', 'Pascal']
student_two.add_courses('OOP')
student_two.grades['Git'] = [10, 20, 30, 40, 50]
student_two.grades['Python'] = [10, 30]
print(student_two)

if student_one.__lt__(student_two):
    print(f'{student_two.name} {student_two.surname} лучший!\n')
else:
    print(f'{student_one.name} {student_one.surname} лучший!\n')

lecturer_one = Lecturer('Bob', 'Hoskins')
lecturer_one.courses_attached += ['Python']
lecturer_one.courses_attached += ['Pascal']
student_one.rate_lecturer(lecturer_one, 'Python', 5)
student_one.rate_lecturer(lecturer_one, 'Pascal', 10)
student_two.rate_lecturer(lecturer_one, 'Python', 12)
student_two.rate_lecturer(lecturer_one, 'Pascal', 10)
# print(lecturer_one.grades)
print(lecturer_one)

lecturer_two = Lecturer('Ashley', 'Gorrel')
lecturer_two.courses_attached += ['Python']
lecturer_two.courses_attached += ['Pascal']
student_one.rate_lecturer(lecturer_two, 'Python', 5)
student_one.rate_lecturer(lecturer_two, 'Pascal', 10)
student_two.rate_lecturer(lecturer_two, 'Python', 13)
student_two.rate_lecturer(lecturer_two, 'Pascal', 5)
# print(lecturer_two.grades)
print(lecturer_two)

if lecturer_one.__lt__(lecturer_two):
    print(f'{lecturer_two.name} {lecturer_two.surname} лучший!\n')
else:
    print(f'{lecturer_one.name} {lecturer_one.surname} лучший!\n')
