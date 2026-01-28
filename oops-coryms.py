import datetime
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        # self.email = first + '.' + last + '@email.com'
        
        Employee.num_of_emps += 1
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @fullname.setter 
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first 
        self.last = last 
    
    def __repr__(self):
        # unambigous representation of the object and should be used for debugging and logging
        
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        # readable representation of the object and is meant to be used as a Display to the end user
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount 
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday() == 6:
            return False
        return True 
    
    
    
class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay,employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('--->', emp.fullname())
        

my_date = datetime.date(2025, 1, 26)
# print(Employee.is_workday(my_date))

emp_1 = Employee("Syed", "Salahuddin", 50000)

emp_2 = Employee("Mohammed", "Azeemuddin", 60000, )

# Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05)

dev1 = Developer('Syed', "Salahuddin", 30000, "Python")

dev2 = Developer("Syed", "Zubair", 40000, "C++")

# print(help(Developer))
mgr_1 = Manager('Sy', 'Sa', 12000, [dev1])
mgr_1.add_employee(dev2)
mgr_1.remove_employee(dev1)
# mgr_1.print_employees()
# print(mgr_1.email)
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
emp_1.first = "Mohammed"
print(emp_1.email)

emp_1.fullname = 'Zubair Yousuf'
print(emp_1.fullname)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1 + emp_2)
# print(dev1.email)
# print(dev2.pay)
# print(dev1.prog_lang)
# print(emp_1.pay)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())

# print(Employee.__dict__)
# print("N")

emp_1.raise_amount = 1.05

# print(emp_1.__dict__)
# # emp_1.apply_raise()
# # print(emp_1.pay)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.num_of_emps)

emp_str_1 = 'MA-JHA-20000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Janfe-Smith-90000'




# emp_3 = Employee.from_string(emp_str_1)
# print(emp_3.email)
# print(emp_3.first)
# print(emp_3.pay)

# print(isinstance(mgr_1, Developer))
# print(issubclass(Manager, Employee))
# print(Employee.fullname(emp_2))

# emp_1.first = "Syed"
# emp_1.last = "Salahuddin"
# emp_1.email = "syedsalahuddin384@gmail.com"
# emp_1.pay = 50000

# emp_2.first = "Mohammed"
# emp_2.last = "Azeemuddin"
# emp_2.email = "mohammedazeem2002@gmail.com"
# emp_2.pay = 60000


# Method --> A Function associated with a class
# Classes --> Allow us to logically group our data and functions in a way that's easy to reuse and also easy to build upon if need to be 

# __init__ --> Constructor / initializer, that runs automatically every time a new object(instance) of a class is Created 

# Each method within a Class automatically takes a instance as the first argument 

# Class Variables are Variables that are shared among all variables of a Class  

# 

# print('{} {} '.format(emp_1.first, emp_1.last))


# --->>> Core OOP Building Blocks <<<----

# Class → A blueprint that defines data (attributes) and behavior (methods)

# Object / Instance → A real-world realization of a class created in memory

# Attribute → A variable that belongs to an object or a class

# Method → A function that is associated with a class and operates on its data

# ---->>Constructors & Initialization <<----
# __init__ → A constructor that runs automatically when a new object is created
# Initialization → The process of assigning initial state to an object
# self → A reference to the current object instance inside the class
# Instance creation → Calling the class name executes __init__

# --->>Instance vs Class Level<<----
# Instance Variable → A variable that belongs to a specific object
# Class Variable → A variable that is shared by all instances of the class
# Namespace → A mapping where Python stores variable names and their objects

# ---->>>Methods Types
# Instance Method → Works with object data and takes self as the first argument
# Class Method → Works with class-level data and takes cls as the first argument
# Static Method → A utility function inside a class that does not access instance or class data

# ----->>>Encapsulation<<<----
# Encapsulation → Bundling data and methods together and controlling access
# Public Members → Accessible from anywhere
# Protected Members (_var) → Intended for internal use (convention-based)
# Private Members (__var) → Name-mangled to avoid accidental access
# Data Hiding → Preventing direct modification of internal state

# ---->>Abstraction<<----
# Abstraction → Showing what an object does, not how it does it
# Abstract Class → A class that cannot be instantiated and defines required methods
# Abstract Method → A method that must be implemented by child classes
# Interface (Python-style) → A contract enforced using abstract base classes

# ---->>>Inheritance<<<-----
# Inheritance → A class deriving behavior and data from another class
# Parent / Base Class → The class being inherited from
# Child / Derived Class → The class that inherits
# Method Overriding → Redefining a parent method in the child class
# super() → Gives access to parent class methods and constructors

# ----->>>>Polymorphism<<<<----
# Polymorphism → Same method name, different behavior depending on object type
# Method Overloading (Python) → Achieved using default arguments or *args
# Method Overriding → Child class changes parent class behavior
# Duck Typing → If it behaves like a duck, Python treats it as one


# ---->>>>Object Lifecycle & Internals<<<----
# Object Creation → Memory allocation + initialization
# Object Identity → Checked using is
# Object Equality → Checked using ==
# Immutability → Object state cannot change after creation
# Mutability → Object state can change without changing identity
# Special (Dunder) Methods

# --->>>Dunder Methods → Special methods that customize object behavior<<<---
# __str__ → Human-readable string representation
# __repr__ → Developer-friendly representation
# __eq__ → Defines equality behavior
# __len__ → Defines behavior for len()

# ----->>>>Operator Overloading → Custom behavior for operators like +, ==, *<<<<-----
# Composition vs Inheritance
# Composition → One class owns another class (HAS-A relationship)
# Inheritance → One class is a specialized version of another (IS-A relationship)
# Favor Composition → Leads to flexible and maintainable designs

# ---->>>Memory & Design Concepts<<<---
# Object Reference → Variables point to objects, not values
# Shared State → Class variables can cause side effects if misused
# Loose Coupling → Classes depend minimally on each other
# High Cohesion → A class does one job well


# Real-World Mapping
# Class → Blueprint
# Object → Actual thing
# Method → Action
# Attribute → Property
# Inheritance → Specialization
# Composition → Ownership
# Polymorphism → Flexibility
