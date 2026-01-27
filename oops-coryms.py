class Employee:
    def __init__(self, first, last, pay, email):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = email 


emp_1 = Employee("Syed", "Salahuddin", 50000, "syedsalahuddin384@gmail.com")

emp_2 = Employee("Mohammed", "Azeemuddin", 50000, "mohdazeemuddin2002@gmail.com")

print(emp_1)
print(emp_2)

emp_1.first = "Syed"
emp_1.last = "Salahuddin"
emp_1.email = "syedsalahuddin384@gmail.com"
emp_1.pay = 50000

emp_2.first = "Mohammed"
emp_2.last = "Azeemuddin"
emp_2.email = "mohammedazeem2002@gmail.com"
emp_2.pay = 60000

