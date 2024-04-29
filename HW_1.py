class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and isinstance(lecturer, Lecturer):
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course].append(grade)
            else:
                lecturer.lecturer_grades[course] = [grade]
            return 'Оценка внесена'
        else:
            return 'Ошибка: Лектор не преподает данный курс или студент не записан на этот курс'

    def avg_grade(self):
        total_grade = sum(sum(grades) for grades in self.grades.values())
        total_course = sum(len(grades) for grades in self.grades.values())
        avg_grade = total_grade / total_course if total_course > 0 else 0
        return avg_grade

    def __str__(self):
        avg_grade = self.avg_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\n' \
                f'Курсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}'

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def avg_grade_in_course(self, students, course):
        students_with_grades = [student for student in students if course in student.grades]
        total_grade = sum(sum(student.grades[course]) for student in students_with_grades)
        total_students_with_grades = sum(len(student.grades[course]) for student in students_with_grades)
        if total_students_with_grades > 0:
            return total_grade / total_students_with_grades
        else:
            return 0


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def avg_grade(self):
        total_grades_lecturer = sum(sum(grades) for grades in self.lecturer_grades.values())
        total_courses_lecturer = sum(len(grades) for grades in self.lecturer_grades.values())
        avg_grade_lecturer = total_grades_lecturer / total_courses_lecturer if total_courses_lecturer > 0 else 0
        return avg_grade_lecturer

    def __str__(self):
        avg_grade = self.avg_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.2f}"

    def avg_grade_for_lecturers(self, lecturers, course):
        total_grades_lecturer = 0
        total_lecturers = 0
        for lecturer in lecturers:
            if course in lecturer.lecturer_grades:
                if lecturer.lecturer_grades[course]:
                    total_grades_lecturer += sum(lecturer.lecturer_grades[course])
                    total_lecturers += 1
        if total_lecturers > 0:
            return total_grades_lecturer / total_lecturers
        else:
            return 0


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Ivan', 'Ivanov', 'Male')
student_2 = Student('Alex', 'Alexandrov', 'Male')
student_1.courses_in_progress += ['Python', 'C++', 'Java']
student_2.courses_in_progress += ['Квантовая физика', 'Физкультура']
student_1.finished_courses += ['SQL', 'SQL2']
student_2.finished_courses += ['Математический анализ']
student_1.grades = {'Python': [9, 9, 10, 10], 'C++': [4, 5, 4, 2], 'Java': [1, 10, 10, 10]}
student_2.grades = {'Математический анализ': [10, 1, 10, 10]}

mentor_1 = Mentor('Adam', 'Smasher')
mentor_2 = Mentor('Tom', 'Jerry')

lecturer_1 = Lecturer('Petr', 'Petrov')
lecturer_2 = Lecturer('Oleg', 'Olegov')
lecturer_1.lecturer_grades = {'Python': [10, 3, 5, 8]}
lecturer_2.lecturer_grades = {'Математический анализ': [1, 2, 4, 8]}

reviewer_1 = Reviewer('Vladimir', 'Vladimirov')
reviewer_2 = Reviewer('Anastasiya', 'Muhova')
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_2.rate_hw(student_2, "Математический анализ", 10)

print(f'Student: \n{student_1}\n')
print(f'Student: \n{student_2}\n')
print(student_1.rate_lecturer(lecturer_1, "Python", 9))
print(student_2.rate_lecturer(lecturer_2, "Бег трусцой", 1))
print(f'\nСредняя оценка student_1 > student_2: {student_1 > student_2}')
print(f'Средняя оценка student_1 < student_2: {student_1 < student_2}')
print(f'Средняя оценка student_1 >= student_2: {student_1 >= student_2}')
print(f'Средняя оценка student_1 <= student_2: {student_1 <= student_2}')
print(f'Средняя оценка student_1 == student_2: {student_1 == student_2}')

print(f'\nMentor: \n{mentor_1}\n')
print(f'Mentor: \n{mentor_2}\n')

print(f'Lecturer: \n{lecturer_1}\n')
print(f'Lecturer: \n{lecturer_2}\n')

print(f'Reviewer: \n{reviewer_1}\n')
print(f'Reviewer: \n{reviewer_2}\n')