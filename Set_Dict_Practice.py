#Creat a dic with key value pair where a key-value must be tupple or list

Dic={
    "Cat":"A small animal",
    "Table":["A piece of furniture","List of facts and figure"]
}

print(Dic)

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# ”python” , “java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

Set={"python" , "java","C++","python","javascript","java","python","java","C++","C"}
print("The total classroom needed: ",len(Set))


#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
"""
Subjects={}
x=int(input("Enter the marks for Math: "))
y=int(input("Enter the marks for Phy: "))
z=int(input("Enter the marks for Chem: "))

Subjects.update({"Math":x})
Subjects.update({"Phy":y})
Subjects.update({"Chem":z})
print(Subjects)
"""

#Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)

set1={9,"9.0"}
print(set1) #Number 1 type of solution

set1={("Int",9),("Float",9.0)}
print(set1) #Number 2 type of solution