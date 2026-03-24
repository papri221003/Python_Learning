class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
c1=Circle(4)

print("The area of the circle is: ",c1.area())

print("The permeter of the circle is: ",c1.perimeter())