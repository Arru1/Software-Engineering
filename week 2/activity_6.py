class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        """Displays employee details."""
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Job Title: {self.job_title}")
    
    def give_raise(self, amount):
        """Increase the employee's salary by the given amount."""
        self.salary += amount
        print(f"{self.name}'s new salary is: ${self.salary:,.2f}")


# Create two employee objects with different data
employee1 = Employee("Ashelsha", 55000, "Software Developer")
employee2 = Employee("Aruna", 60000, "Project Manager")

# Display info for both employees
print("Employee 1 Info:")
employee1.display_info()
print("\nEmployee 2 Info:")
employee2.display_info()

# Give both employees a raise and display updated salaries
print("\nApplying raises...\n")
employee1.give_raise(5000)  # Ashlesha gets a $5,000 raise
employee2.give_raise(7000)  # Aruna gets a $7,000 raise
