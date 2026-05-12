# AIM:
# To write a Python program demonstrating advanced OOP concepts including Encapsulation 
# (private variables), Inheritance, Polymorphism (Operator Overloading), the @property 
# decorator, @classmethod, and object deletion using an Employee Management System.

print("=== EMPLOYEE MANAGEMENT SYSTEM ===", end="\n\n")

class Employee:
    company_name = "TCS / Infosys"
    emp_count = 0

    def __init__(self, name, basic_salary):
        self.name = name
        self.__basic_salary = basic_salary 
        Employee.emp_count += 1 # alternate way: self.__class__.emp_count += 1

    @classmethod
    def show_total_employees(cls):
        print(f"Total Employees in {cls.company_name}: {cls.emp_count}")

    @property
    def total_salary(self):
        return self.__basic_salary + (self.__basic_salary * 0.10)

class Manager(Employee):
    def __init__(self, name, basic_salary, department):
        super().__init__(name, basic_salary) # alternate way: Employee.__init__(self, name, basic_salary)
        self.department = department

    def __add__(self, other):
        return self.total_salary + other.total_salary

    def __gt__(self, other):
        return self.total_salary > other.total_salary
    
    def __del__(self):
        Employee.emp_count -= 1

m1 = Manager("Ashu", 50000, "IT")
m2 = Manager("Rahul", 40000, "HR")

print(f"{m1.name} Total Salary: ₹{m1.total_salary}")
print(f"{m2.name} Total Salary: ₹{m2.total_salary}\n")

print(f"Total Salary Expense of both: ₹{m1 + m2}")

if m1 > m2:
    print(f"{m1.name} earns more than {m2.name}.\n")
else:
    print(f"{m2.name} earns more.\n")

Employee.show_total_employees() # alternate way: m1.show_total_employees()

# Accessing private variable (Name Mangling hack)
# print(m1.__basic_salary) # alternate way to bypass error: print(m1._Employee__basic_salary)
print(m1._Employee__basic_salary)
m1.show_total_employees() # it will work like Employee.show_total_employees() bcuz  inheritance


print("\nFiring (Deleting) Rahul from the company...")
del m2    #point to remember that del is keyword it will first delete the m2 then it will call __del__()  , it doesnt call
#          directly that why first m2 will delete than the decrement will be done as per the dumper function , del removes the reference variable.
#          If no references remain, Python destroys the object and automatically calls __del__().

Employee.show_total_employees()
m1.show_total_employees() 

print(m1.name)
# print(m2.name) #error bcuz we have delete the m2

del m1 
Employee.show_total_employees()

# m1.show_total_employees() # error bcuz m1 is del 

m3 = Employee("x",10)
m4 = Employee("y",20)

m4.show_total_employees() #2 , m3 or m4 both will show 2 
Employee.show_total_employees() #2 same 
del m4

Employee.show_total_employees() # output will be 2 only bcuz we change __del__ in child not in parent 

'''
Output :
 
=== EMPLOYEE MANAGEMENT SYSTEM ===

Ashu Total Salary: ₹55000.0
Rahul Total Salary: ₹44000.0

Total Salary Expense of both: ₹99000.0
Ashu earns more than Rahul.

Total Employees in TCS / Infosys: 2
50000
Total Employees in TCS / Infosys: 2

Firing (Deleting) Rahul from the company...
Total Employees in TCS / Infosys: 1
Total Employees in TCS / Infosys: 1
Ashu
Total Employees in TCS / Infosys: 0
Total Employees in TCS / Infosys: 2
Total Employees in TCS / Infosys: 2
Total Employees in TCS / Infosys: 2'''