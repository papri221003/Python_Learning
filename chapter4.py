#DICTIONARY AND SET

#Nested dictionary
"""
students_marks={
    "English":97,
    "arts_group":{
        "Bengali":85,
        "Geography":99,
        "History":86,
        "Sanskrit":90
    },
   "Science_group":{
        "Maths":95,
        "Physics":90,
        "Biology":96,
        "Comp. sci":90
    }
}

print(students_marks["arts_group"]["Bengali"])

print(list(students_marks.keys()))
print(list(students_marks.values()))
pairs=list(students_marks.items())
print(pairs[1])

#Suppose you are given a list of subjects...each subject must have only one clsroom needed.tell how many classrooms are needed for the subject

list=["python","java","c++","python","javascript","java","python","java","c++","c"]

new_set=set(list)
print("The number of classrooms are needed: ",len(new_set))
"""
new_dict={}

x=int(input("Enter the marks for maths: "))
y=int(input("Enter the marks for phy: "))
z=int(input("Enter the marks for chem: "))

new_dict.update({"maths":x})
new_dict.update({"phy":y})
new_dict.update({"chem":z})

print(new_dict)