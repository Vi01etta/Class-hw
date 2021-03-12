#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

first_mentor = Mentor('Alexandr', 'Vinogradov')
first_mentor.courses_attached += ['Python']

second_mentor = Mentor('Popova', 'Elena')
second_mentor.courses_attached += ['Python']

lecturer_list = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        lecturer_list.append(self)

    def __str__(self):  
        return f"Имя: {self.name}\n"                f"Фамилия: {self.surname}\n"                f"Средняя оценка за лекции: {self.average_grade}"

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    @property
    def average_grade(self):
        return sum(self.grades) / len(self.grades)


first_lecturer = Lecturer("Eugeny", "Petrov")
first_lecturer.courses_attached = ['Java', 'Web', 'Python', 'Git']

second_lecturer = Lecturer('Zina', 'Ivanova')
second_lecturer.courses_attached = ['Git', 'Python']

student_list = []
class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)


    def rate_lecturing(self, lecturer, course, grade):
         if isinstance(
                 lecturer, Lecturer
         ) and course in lecturer.courses_attached and course in self.courses_in_progress:
             lecturer.grades.append(grade)
         else:
             return 'Ошибка'


    def __str__(self):
        return f"Имя: {self.name}\n"               f"Фамилия: {self.surname}\n"               f"Средняя оценка за домашние задания: {self.average_grade}\n"               f"Курсы в процессе изучения: {self.courses_in_progress}\n"               f"Завершенные курсы: {self.finished_courses}"
               
    
    @property
    def average_grade(self):
      values_sum = sum([sum(values_list) for values_list in self.grades.values()])
      values_len = sum([len(b) for a,b in self.grades.items()])
      return values_sum / values_len


    def __lt__(self, other):
        return self.average_grade < other.average_grade



first_student = Student('Vlasov', 'Ivan', 'male')
first_student.courses_in_progress += ['Web', 'Git']
first_student.finished_courses += ['java', 'Python']

second_student = Student('Vika', 'Lenina', 'female')
second_student.courses_in_progress += ['Python', 'Git']
second_student.finished_courses += ['java', 'Web']



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n"                f"Фамилия: {self.surname}"


first_reviewer = Reviewer('Stepanova', 'Lada')
first_reviewer.courses_attached += ['Python', 'Git', 'Web']

second_reviewer = Reviewer('Fadeev', 'Abram')
second_reviewer.courses_attached += ['Git', 'Python']


first_reviewer.rate_hw(first_student, 'Web', 9)
first_reviewer.rate_hw(first_student, 'Git', 8)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 7)

first_student.rate_lecturing(first_lecturer, 'Git', 10)
first_student.rate_lecturing(first_lecturer, 'Web', 7)
second_student.rate_lecturing(second_lecturer, 'Python', 9)
second_student.rate_lecturing(second_lecturer, 'Git', 9)

# print(first_student)
# print(second_student)
# print(first_reviewer)
# print(second_reviewer)
# print(first_lecturer)
# print(second_lecturer)

# print(first_student > second_student)
# print(first_lecturer < second_lecturer)



def aver_hw_gr(course):
    '''реализовать функцию для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса.'''
    
    st_list = student_list.copy()
    sum_hw = 0
    for student in st_list:
        if course in student.courses_in_progress:
            sum_hw += sum(student.grades[course]) / len(student.grades[course])
    return sum_hw / len(st_list)


def aver_lect_gr(course):
  '''реализовать функцию для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса.'''
  lect_list = lecturer_list.copy()
  sum_lr = 0
  for lecturer in lect_list:
    if course in lecturer.courses_attached:
      sum_lr += sum(lecturer.grades) / len(lecturer.grades)
  return sum_lr / len(lect_list)

print(aver_lect_gr("Git"))
print(aver_hw_gr('Git'))

