from task5 import Person

class Student(Person):
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

    def display_info(self):
        super().display_info()
        print(f"Academic Record: {self.academic_record}")

    def updated_info(self, new_record):
        self.academic_record = new_record
        print(f"Updated Academic Record: {self.academic_record}")

# Example usage:

student = Student("Ram", "123 Uni Rd", 20, "R123", "GPA: 2.8")
student1 = Student("Shyam", "1234 Uni Rd", 22, "S1234", "GPA:4.0")

print("Before update:")
student.display_info()
student1.display_info()

print("\nUpdating academic record...")
student.updated_info("A+")
student1.updated_info("B+")

print("\nAfter update:")
student.display_info()
student1.display_info()
