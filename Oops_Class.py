"""
class Student:
    cls=12
    sem="second"
    
s1=Student()
s1.name="Papri"
s1.age=20
print(s1.name)
print(s1.cls)

"""

#Constructor

class Student:
    clg_name="ABC college"
    name="Anoymous"
    
    def __init__(self,name):
        self.name=name
        print("Name of the student is: ",self.name)
        

S1=Student("Papri")