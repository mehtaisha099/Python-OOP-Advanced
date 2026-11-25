class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Teacher(Person):
    def teach(self):
        print("Teacher teaches students")


class Student(Person):
    def study(self):
        print("Student studies")


teacher = Teacher("Mr. Patel")
student = Student("Isha")

teacher.show_name()
teacher.teach()

student.show_name()
student.study()