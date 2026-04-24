'''
Write a Python program to perform the following operations sequentially on a text file:

1. Create a new file named diary.txt and write the first entry: "Diary Entry 1: I started 
learning File I/O in Python today."
2. Add a second entry to the exact same file without deleting the first entry: 
"Diary Entry 2: Using the 'with' syntax makes file handling very easy." (Ensure it appears 
on a new line).
3. Read the complete content of the file and display it on the console.

(Use the 'with' syntax for all file operations).
'''

with open("diary.txt" ,"w") as f:
    f.write("Diary Entry 1: I started learning File I/O in Python today.")

with open("diary.txt","a") as f:
    f.write("\nDiary Entry 2: Using the 'with' syntax makes file handling very easy.")

with open("diary.txt","r") as f:
    data=f.read()
    print(data)

def add_string():
    stringg=input("Enter a string to add: ")
    f = open("diary.txt","a")
    f.write("\n" + stringg)
    f.close()
    return stringg
add_string()
print(add_string())

def replace_word():
    word = input("Enter A word to replace: ")
    withwhatword = input("Enter a word to replace with: ")
    with open("diary.txt","r") as f :
        data=f.read()
        if(data.find(word) != -1):
            print("Replaced Sucessfull.")
            print("\n" + data.replace(word,withwhatword))
            with open("diary.txt","w") as f :
                f.write(data.replace(word,withwhatword))
            return data.replace(word,withwhatword)

        else :
            print(f"Word '{word}' is not present.")
replace_word()
print(replace_word())
