# My comment

"""
Multiline
comment
"""

a = 1
b = 2
print(a+b)

c = "hello"
print(c)

b = c
print(c)

#List []
d = ["Item 0", "Item 1"]
print(d)

d = d + ["Item 3"]
print(d)

#Dictionary {}
e = {"Favorite color" : "Green"}
print(e["Favorite color"])

#Set {} - does not repeat values
f = {1,2,3,3,4,6,7,7,7}
print(f)

if 1 == 1:
    print("It is true")

#Loop (inclusive,exclusive)
for item in d:
    print(item)

for i in range(0,5):
    print(i)

#While loop
g = 5
while g > 0:
    print(g)
    g -= 1

#Object or essentially a Struct
class Employee:

    #Class variables
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@Company.com"

    #Method within the class
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    #Use self.raise_amount to allow for individual instance alterations -- Employee.raise_amount to inherit from class
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    #Class methods related to attributes/variables of the class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #Split used in class method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")#Example tuple
        return cls(first, last, pay)

    #Static method -- not related to any attribute/variable of the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#Inheritence -- put in () what class to inherit from
class Developer(Employee):
    raise_amount = 1.10 #will only effect this subclass

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #will let Employee class handle this info
        self.prog_lang = prog_lang #only the developer object will ask for this parameter


Employee.set_raise_amt(1.05) #Is used for changes to the class

emp_1 = Developer("James", "Legg", 50000, "Python")
#1st way
print(emp_1.fullname())
#2nd way
print(Employee.fullname(emp_1))
#3rd full dict
print(emp_1.__dict__)

#Datetime yyyy/mm/dd -- datetime has a weekday method monday = 0 and sunday = 6
import datetime
my_date = datetime.date(2021, 6, 12)

print(Employee.is_workday(my_date))

#Split used in Class method
emp_str_1 = "John-Doe-70000"
emp_4 = Employee.from_string(emp_str_1)
print(emp_4.first)
print(emp_4.pay)
print(emp_1.prog_lang)

#Modules
import math
print(math.pi)

#Enum
from enum import Enum
class Card (Enum):
    DIAMOND = 1
    HEART = 2
    SPADE = 3
    CLUBS = 4
print(Card.CLUBS.value)

#------------------------------------ Troubleshooting

#'Help' will show method resolution order
#print(help(Developer))

#'isinstance' will show if instance is an instance of a class -- (instance, class)
#print(isinstance(emp_1, Employee))

#'issubclass' will show if class is an subclass of a class -- (subclass, class)
#print(issubclass(emp_1, Employee))

