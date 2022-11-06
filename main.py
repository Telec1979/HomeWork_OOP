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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.add_courses('GIT')
#best_student.grades['Git'] = [10, 10, 10, 10, 10]
#best_student.grades['Python'] = [10, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
# print(best_student.finished_courses)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['GIT']
# print(cool_mentor.courses_attached)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 20)
# cool_mentor.rate_hw(cool_mentor, 'GIT', 22)
# cool_mentor.rate_hw(best_student, 'GIT', 10)
#
print(best_student.grades)