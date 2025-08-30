# Base class
class Person:
    def __init__(self, name, address, age, ID):
        self.name = name                      # Public attribute
        self._address = address               # Protected attribute (by convention)
        self.age = age                        # Public attribute
        self.__ID = ID                        # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Address: {self._address}, Age: {self.age}")
        print(f"ID (from method): {self.__ID}")  # Accessing private attribute internally

    def get_ID(self):  # Public method to access private attribute
        return self.__ID


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


# New Class to Demonstrate Public, Protected, and Private Access
class UniversityMemberDemo:
    def __init__(self, person: Person):
        self.person = person

    def access_attributes(self):
        print("\n[Accessing attributes from outside the class]")

        # Public attribute: accessible
        print(f"Public name: {self.person.name}")

        # Protected attribute: accessible (by convention should not be accessed)
        print(f"Protected address: {self.person._address}")

        # Private attribute: not directly accessible
        try:
            print(f"Private ID: {self.person.__ID}")  # Will raise AttributeError
        except AttributeError:
            print("Private ID: Cannot access directly (__ID is private)")

        # Correct way to access private attribute
        print(f"Private ID (using method): {self.person.get_ID()}")


# Creating instances
student = Student("Ram", "123 Uni Rd", 20, "R123", "GPA: 3.8")
academic = Academic("Dr. Arun", "45 Faculty Ln", 45, "A456", "TX001", 80000)
staff = GeneralStaff("Makai", "78 Admin St", 38, "M789", "TX002", 25)

# Displaying information
student.display_info()
print()
academic.display_info()
print()
staff.display_info()

# Demonstrating access modifiers
demo = UniversityMemberDemo(student)
demo.access_attributes()
