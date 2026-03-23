"""
class Student:
    name="Annoymous"
    @classmethod
    def changeName(cls,name):
       #self.name=name  (To change the class method we use classmethod
       
       cls.name=name
        
        
c1=Student()
c1.changeName("Papri")
print(c1.name)
print(Student.name)

"""

#Property decorator

class Student:
    
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem
        
    @property
    def percentage(self):
        return (self.phy+self.chem+self.math)/3
    
c1=Student(95,96,98)
print(c1.percentage)
c1.math=90
print(c1.percentage)