'''Write a Python program to manage a college library system by initializing and updating a 
dictionary with book records (names and prices) using both bracket notation and the update()
method, including taking dynamic user input. Additionally, the program must utilize a list to
record student borrowers and convert it into a Set to extract, display, and count the total
number of unique students.'''

bookdict= {}

bookdict["python"] = 100
bookdict.update({"java":70})

n = int(input("How many book you have to enter: "))

for i in range(n):
    name = input(f"Enter Book{i} Name: ")
    price= int(input(f"Enter Book{i} Price: "))
    bookdict.update({name : price}) # Simple method bookdict[name]=price

borrowlist = []
ns=int(input("Enter no. of student: "))
for j in range(ns):
    borrowlist.append(input(f"Enter the name of {j} borrower name: "))
setlist = set(borrowlist)
print("Set of student borrowers are: ", setlist)
print("Total no. of unique students is: ", len(setlist))
print(bookdict)