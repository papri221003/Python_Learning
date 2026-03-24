class Order:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def __gt__(self,o2):
        return self.price>o2.price
    
o1=Order("conflower",84)

o2=Order("Tea",80)
print("The price of o1 is greather or not: ")
print(o1>o2)