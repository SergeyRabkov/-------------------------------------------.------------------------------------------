class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __get_average_grade(self):
        count_grade = 0
        sum_grade = 0
        for _ in range(len(self.grades.keys())):
            for value in self.grades.values():
                count_grade += len(value)
                sum_grade += sum(value)
        return round(sum_grade / count_grade, 1)
                
    def __str__(self):
        res = f'''Имя: {self.name}
Фамелия: {self.surname}
Средняя оценка за домашние задания: {self.__get_average_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
        return res
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student!'
        return self.__get_average_grade() > other.__get_average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамелия: {self.surname}\n'
        return res

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def __get_average_grade(self):
        for value in self.grades.values():
            return round(sum(value) / len(value), 1)
    
    def __str__(self):
        res = super().__str__()+f'Средняя оценка за лекции: {self.__get_average_grade()}\n'
        return res
        
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer!'
        return self.__get_average_grade() > other.__get_average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def get_students_average_grade(students, course):
    all_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            all_grades += student.grades[course]
    if len(all_grades) == 0:
        res = 'Ошибка'
    else:
        res = f'Средняя оценка за домашние задания по всем студентам в рамках {course} курса = {round(sum(all_grades) / len(all_grades), 1)}'
    return res

def get_lecturers_average_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            all_grades += lecturer.grades[course]
    if len(all_grades) == 0:
        res = 'Ошибка'
    else:
        res = f'Средняя оценка за лекции всех лекторов в рамках {course} курса = {round(sum(all_grades) / len(all_grades), 1)}'
    return res

students_list = []
lecturers_list = []

python_lecturer = Lecturer('Python', 'Buddy')
python_lecturer.courses_attached += ['Python']
lecturers_list.append(python_lecturer)

git_lecturer = Lecturer('Git', 'Buddy')
git_lecturer.courses_attached += ['Git']    
lecturers_list.append(git_lecturer)

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
students_list.append(best_student)
best_student.rate_hw(python_lecturer, 'Python', 10)
best_student.rate_hw(python_lecturer, 'Python', 9)
best_student.rate_hw(python_lecturer, 'Python', 8)
best_student.rate_hw(git_lecturer, 'Git', 10)
best_student.rate_hw(git_lecturer, 'Git', 9)
best_student.rate_hw(git_lecturer, 'Git', 9)

worst_student = Student('Pol', 'Eman', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Git']
worst_student.finished_courses += ['Введение в программирование']
students_list.append(worst_student)
worst_student.rate_hw(python_lecturer, 'Python', 7)
worst_student.rate_hw(python_lecturer, 'Python', 8)
worst_student.rate_hw(python_lecturer, 'Python', 5)
worst_student.rate_hw(git_lecturer, 'Git', 8)
worst_student.rate_hw(git_lecturer, 'Git', 8)
worst_student.rate_hw(git_lecturer, 'Git', 8)

python_reviewer = Reviewer('Some', 'Python') 
python_reviewer.courses_attached += ['Python']
python_reviewer.rate_hw(best_student, 'Python', 10)
python_reviewer.rate_hw(best_student, 'Python', 9)
python_reviewer.rate_hw(best_student, 'Python', 8)
python_reviewer.rate_hw(worst_student, 'Python', 7)
python_reviewer.rate_hw(worst_student, 'Python', 6)
python_reviewer.rate_hw(worst_student, 'Python', 5)

git_reviewer = Reviewer('Some', 'Git') 
git_reviewer.courses_attached += ['Git']
git_reviewer.rate_hw(best_student, 'Git', 10)
git_reviewer.rate_hw(best_student, 'Git', 9)
git_reviewer.rate_hw(best_student, 'Git', 10)
git_reviewer.rate_hw(worst_student, 'Git', 4)
git_reviewer.rate_hw(worst_student, 'Git', 8)
git_reviewer.rate_hw(worst_student, 'Git', 6)

print(python_reviewer)
print(git_reviewer)
print(python_lecturer)
print(git_lecturer)
print(best_student)
print(worst_student)
print(best_student > worst_student)
print(python_lecturer > git_lecturer)
print(python_lecturer > best_student)
print(best_student > git_lecturer)

print(get_lecturers_average_grade(lecturers_list, 'Python'))
print(get_lecturers_average_grade(lecturers_list, 'Git'))
print(get_students_average_grade(students_list, 'Python'))
print(get_students_average_grade(students_list, 'Git'))
