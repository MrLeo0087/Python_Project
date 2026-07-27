'''2. Student Grade Calculator
Concepts: Classes + methods
A Student class that stores subjects and marks. Calculate average and assign a grade (A/B/C...).
Hints:
- Use a dictionary inside the object: self.marks = {} to store subject -> mark.
- Add both an instance method calculate_average() and a class method to track total students created.
- Think about where the grade boundaries (90=A, 80=B...) should live - as constants on the class.

DATE : Thursday, July 23, 2026  
'''

class Student:
    total_student = 0
    GRADE = {90:'A',80:'B',70:'C',60:'D',50:'E',40:'E'}
    # subject = ['math','science','nepali','english','health','arts']
    subject = ['math','science']
    

    def __init__(self):
        self.marks = {}
        self.avg = 0
        self.grade = 'F'

        Student.total_student +=1
        self.take_input()
        self.calculate_average()
        self.assign_grade()
        self.show_result()
        

    def take_input(self):

        for i in Student.subject:
            subject_mark = int(input(f'Enter mark of {i} :'))
            self.marks[i] = subject_mark
    
    def calculate_average(self):
        total_sum = 0
        for i in self.marks:
            total_sum += self.marks[i]

        self.avg = total_sum/len(Student.subject)

    def assign_grade(self):
        keys = sorted(Student.GRADE.keys(), reverse=True)


        for i in keys:
            if self.avg >= i: 
                self.grade = Student.GRADE[i]
                break


    def show_result(self):
        print('--'*50)
        print(f'This is {Student.total_student} student')
        print(f'Average of student mark : {self.avg}')
        print(f'Grade of student : {self.grade}')
        print('--'*50)





user1 = Student()
user2 = Student()
user4 = Student()
user5 = Student()
            
