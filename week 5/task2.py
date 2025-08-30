from task import Person
class Student(Person):
    def __init__(self, name, address, age, ID):
         super().__init__(name, address, age, ID)
         #Person.__init___(name.address,age)
         #self.name=name
         #self.address=address
         #self.age=age
         self.ID=ID
        
    def greet(self):
         print(f"Greetings and felicitation from the maestro {self.name}")
         
student1=Student("Aruna","Banepa",23,"AK2")
student1.greet()
