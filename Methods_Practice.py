class Student:
    clg_name="ABC COLLEGE"
    @staticmethod
    def greet():
        print("Welcome! in the new college")
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        i=0
        while(i<len(self.marks)):
            sum+=self.marks[i]
            i+=1
        
        print("Hi!!",self.name,"your avg score is: ",sum/3) 
    
       
        
s1=Student("Trisha",[95,96,97])
s1.greet()

s1.get_avg()