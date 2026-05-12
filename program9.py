'''
Write a Python program to build a 'Smart Student Portal' using Object-Oriented Programming 
(OOP). The program must demonstrate the following concepts:

1. Class Attribute: Create a Student class and define a class attribute school_name (e.g.,
 "Apna College") which is common for all students.
2. Constructor & Instance Attributes: Use the __init__ method with the self parameter to 
assign a name and a list of marks (for 3 subjects) to each student object.
3. Instance Method: Create a method get_average() that calculates the average of the 
student's marks and prints a personalized result showing their name, school name, and 
average score.
4. Static Method: Use the @staticmethod decorator to create a method portal_greeting() 
that prints a general welcome message and school rules (without taking the self parameter).
5. Execution: Create at least two different student objects, call the static method once, 
and call the get_average() method for both students
'''

print("\n===OOPS Concept===", end="\n\n")

class Student:
    school = "OOPS IN PYTHON"

    def __init__(self,name,marks):
        self.Studentname = name
        self.studmarks = marks

    def getavg(self):
        sum=0
        for i in self.studmarks:
            sum += i
        print(f"Student Name: {self.Studentname} from {Student.school} has average score: {sum/3}.")
    
    @staticmethod
    def portal_greeting():
        print("This is a static class , without self parameter .")

s1 = Student("Ashu", [96,99,92])
s2 = Student("Yadav", [86,89,95])

s1.portal_greeting()
print(s1.Studentname)
print(s2.studmarks)

s1.getavg()
s2.getavg()