'''Write a Python program to analyze a list of raw text tags. The program must extract and 
store all unique tags from the list using an appropriate data structure. It should also 
create a key-value data structure to map each unique tag to its occurrence frequency in the
original list. Finally, the program must insert a new tag, "deep learning", into the unique
collection and add it to the frequency mapping with a value of 1, displaying both 
data structures at the end.'''

total_tags = int(input("Enter total no. of tags: "))

rawdata = []
for i in range(total_tags):
    rawdata.append(input(f"Enter the raw tag {i}: "))

uniquedata = set(rawdata)

mapdata = {}
for tags in rawdata:
    mapdata.update({tags : rawdata.count(tags)}) # or in simple way, mapdata[tags] : rawdata.count(tags)

uniquedata.add("deep leaning")
mapdata["deep learning"] =  1

print("Final output after all operation .")
print("Unique Tags are: " , uniquedata)
print("Tags with there counts: ", mapdata)