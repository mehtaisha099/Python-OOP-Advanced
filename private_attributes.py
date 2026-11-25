class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student = Student()

student.set_marks(85)

print("Marks:", student.get_marks())