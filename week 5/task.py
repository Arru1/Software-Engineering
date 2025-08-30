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
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

    def display_info(self):
        super().display_info()
        print(f"Academic Record: {self.academic_record}")


# Subclass: Academic
class Academic(Person):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}, Salary: ${self.salary}")


# Subclass: GeneralStaff
class GeneralStaff(Person):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}, Pay Rate: ${self.pay_rate}/hr")

student = Student("Ram", "123 Uni Rd", 20, "R123", "GPA: 3.8")
academic = Academic("Dr. Arun", "45 Faculty Ln", 45, "A456", "TX001", 80000)
staff = GeneralStaff("Makai", "78 Admin St", 38, "M789", "TX002", 25)

student.display_info()
print()
academic.display_info()
print()
staff.display_info()