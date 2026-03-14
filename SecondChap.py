"""
4name=input("Enter the First name: ")

print("Length of the name is: ",len(name))

print("Occurence of $ in the string: ",name.find('$'))
"""

#WAP to find greatest of three numbers entered by the user

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if((num1>num2) & (num1>num3)):
    print("The greatest number is: ",num1)
elif((num2>num1) & (num2>num3)):
    print("The greatest number is: ",num2)
else:
    print("The greatest number is: ",num3)