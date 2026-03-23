class Car:
    def __init__(self,type):
        self.type=type
        print(self.type)
        
    @staticmethod
    def start():
        print("The car has been started.......")
        
    @staticmethod
    def stop():
        print("The car has been stopped!......")
        

class ToyotaCar(Car):
    
    def __init__(self,name,type):
        self.name=name
        print(self.name)
        
        super().start()
        super().__init__(type)
        
    
c1=ToyotaCar("Fortuner","electric")

