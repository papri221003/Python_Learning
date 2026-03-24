class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
        
    def showDetails(self):
        print("the role is: ",self.role)
        print("The department is: ",self.department)
        print("The salary is: ",self.salary)
        

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Data analyst","analyst",33000)
        
    def showInfoEngi(self):
        print("The name is: ",self.name,"and the age is: ",self.age)
        
        
em=Engineer("Papri",24)

em.showInfoEngi()
em.showDetails()
