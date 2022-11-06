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
             f'Средняя оценка за домашние задания: {average(self.grades)}\n' \
             f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
             f'Завершенные курсы: {", ".join(self.finished_courses)}  '
        return res


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
              f'Средняя оценка за лекции: {average(self.grades)} '
        return res


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
              f'Фамилия: {self.surname}'
        return res


some_reviewer = Reviewer('Bob', 'Hoskins')
print(some_reviewer)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python', 'GIT']
best_student.add_courses('GIT')
#best_student.grades['Git'] = [10, 10, 10, 10, 10]
#best_student.grades['Python'] = [10, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
# print(best_student.finished_courses)

cool_lector = Lecturer('Some', 'Buddy')
cool_reviewer = Reviewer('Some_r', 'Buddy_r')
cool_reviewer.courses_attached += ['Python']
cool_lector.courses_attached += ['GIT']
print(cool_lector.courses_attached)
best_student.rate_lecturer(cool_lector, 'GIT', 8) # выставляем оценку лектору
print(cool_lector.grades) # проверяем
print(cool_lector)

cool_reviewer.rate_hw(best_student, 'Python', 10) # ставим оценку студенту
# cool_mentor.rate_hw(best_student, 'Python', 20)
# cool_mentor.rate_hw(cool_mentor, 'GIT', 22)
# cool_mentor.rate_hw(best_student, 'GIT', 10)
#
print(best_student.grades)
print(best_student)