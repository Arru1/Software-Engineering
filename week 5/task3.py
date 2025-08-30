# Base class
class Person:
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID

    def display_info(self):
        print(f"Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.ID}")


# Subclass: Student
class Student(Person):
    def __init__(self, name, address, age, ID, academic_record, course=None):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record
        self.course = course  # Can be a Course object

    def display_info(self):
        super().display_info()
        print(f"Academic Record: {self.academic_record}")
        if self.course:
            print("Course Info:")
            self.course.display_info()


# Subclass: Academic
class Academic(Person):
    def __init__(self, name, address, age, ID, tax_code, salary, course=None):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary
        self.course = course  # Academics may teach courses

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}, Salary: ${self.salary}")
        if self.course:
            print("Teaching Course:")
            self.course.display_info()


# Subclass: GeneralStaff
class GeneralStaff(Person):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}, Pay Rate: ${self.pay_rate}/hr")


# New Class: Course
class Course:
    def __init__(self, code, name, credit_hours):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours

    def display_info(self):
        print(f"Course Code: {self.code}, Course Name: {self.name}, Credit Hours: {self.credit_hours}")


# Create course instances
course1 = Course("CS101", "Introduction to Programming", 3)
course2 = Course("MATH201", "Calculus II", 4)

# Create people and associate them with courses
student = Student("Ram", "123 Uni Rd", 20, "R123", "GPA: 3.8", course1)
academic = Academic("Dr. Arun", "45 Faculty Ln", 45, "A456", "TX001", 80000, course2)
staff = GeneralStaff("Makai", "78 Admin St", 38, "M789", "TX002", 25)

# Display info
student.display_info()
print()
academic.display_info()
print()
staff.display_info()
