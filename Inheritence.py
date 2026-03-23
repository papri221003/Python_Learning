


"""
    Single Inheritence
    class Car:
    @staticmethod
    def start():
        print("The car has been started.......")
        
    @staticmethod
    def stop():
        print("The car has been stopped!......")
        

class ToyotaCar(Car):
    
    def name(self,name):
        self.name=name
        print(self.name)
        
    
c1=ToyotaCar()

c1.name("fortuner")
c1.start()

    """
    
#Multi_level

class Car:
    @staticmethod
    def start():
        print("The car has been started.......")
        
    @staticmethod
    def stop():
        print("The car has been stopped!......")
        

class ToyotaCar(Car):
    
    def name(self,brand):
        self.brand=brand
        print(self.brand)
        
class fortuner(ToyotaCar):
    def speed(self,speed):
        self.speed=speed
        print(self.speed)
        
    
c1=fortuner()

c1.speed("24kmph")
c1.start()
c1.name("Toyota")


    
    