Student={
    "Name":"Papri",
    "Age":22,
    "CGPA":8.76,
    "Subjects_score":{
        "Chem":96,
        "Math":95,
        "Phy":"74"
    }
}

Student["Name"]="Niladri"
Student["DOB"]="11.04.04"
print(Student)
print(Student["Subjects_score"]["Phy"])

#Dictionary Methods
print(list(Student.keys()))

print(list(Student.values()))

Item_list=list(Student.items())
#print(list(Student.items()))
print(Item_list[1])

