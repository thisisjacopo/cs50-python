#Lists are indexed starting at 0
students = ["Harry", "Ron", "Hermione", "Ginny", "Fred", "Neville", "Draco"]
houses = ["Slytherin", "Gryffindor", "Ravenclaw", "Hufflepuff"]

for student in students:
    print(student)
    
#using range() and len() to iterate through a list using a for loop using numeric values
for i in range(len(students)):
    print(i, students[i])
    
#dictionary is a collection of key-value pairs that are unordered, changeable, and indexed (like a hash table) 
# and do not allow duplicates (like sets)
#keys are unique and immutable (like sets)

students_dict = {
    "Harry": "Gryffindor", 
    "Draco": "Slytherin",
    "Luna": "Ravenclaw",
    "Cedric": "Hufflepuff",
    "Hermione": "Gryffindor",
    "Fred": "Gryffindor",
    "Neville": "Gryffindor",
    "Ginny": "Gryffindor",
    "Ron": "Gryffindor"
}

print(students_dict["Harry"])

#for loop to iterate through a dictionary
for student in students_dict:
    print(student, students_dict[student], sep=": ")


#list of dictionaries (list of objects) 
students_list_dict = [
{"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
{"name": "Draco", "house": "Slytherin", "patronus": None},
{"name": "Luna", "house": "Ravenclaw", "patronus": "hare"},
{"name": "Cedric", "house": "Hufflepuff", "patronus": None},
{"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
{"name": "Fred", "house": "Gryffindor", "patronus": None}
]

for student in students_list_dict:
    print(student["name"], student["house"], student["patronus"], sep=", ")