class Complex:
    
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,c2):
        newReal=self.real+c2.real
        newImg=self.img+c2.img
        newNumber=Complex(newReal,newImg)
        return newNumber
    
    def __sub__(self,c2):
        newReal1=self.real-c2.real
        newImg1=self.img-c2.img
        newNumber1=Complex(newReal1,newImg1)
        return newNumber1
    
        
        
c1=Complex(7,8)
c1.showNumber()

c2=Complex(1,5)
c2.showNumber()

c3=c1+c2
c3.showNumber()

c4=c1-c2
c4.showNumber()