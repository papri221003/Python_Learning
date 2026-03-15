"""
def Calc_Avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg

x=int(input("Enter the marks of the Physics: "))
y=int(input("Enter the marks of the Math: "))
z=int(input("Enter the marks of the Chem: "))

print("The avg marks of Physics,Chemistry and Math is: ",Calc_Avg(x,y,z))
"""


#Default parameter Function

def sum(a=4,b=5):
    return a+b

print(sum())


def sum2(a,b=5):
    return a+b

print(sum2(1))


