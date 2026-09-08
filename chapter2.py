"""
#WAP to input users first name and print its length
name=input("Enter the first name of the user : ")
print("The length of the string is:" , len(name))


#WAP to find the occurance of 'i' in a string
string=input("Enter the sentence : ")
print("Number of first occurence of 'a' in the sentence",string.find('a'))
print("The number of occurence of 'a' in the string is: ",string.count('a'))


#Grading system
marks=int(input("Enter the marks of the student: "))

print("Grading System in school.\nGrade of the student is: ")
if(marks>=90):
    print('A')
elif(marks<90 and marks>=80):
    print('B')
elif(marks<80 and marks>=70):
    print('C')
else:
    print('D')
    
    
#WAP to check if a number entered by user is odd or even
num=int(input("Enter the number: "))

print("Detect the number is even or odd.")

if(num%2==0):
    print("Even")
else:
    print("Odd")

#WAP to find the greatest of 3 numbers entered by the user
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

if(n1>=n2 and n1>=n3):
    print("The greatest number is: ",n1)
elif(n2>=n3):
    print("The greatest number is: ",n2)
else:
    print("The greatest number is: ",n3)
    
"""
# WAP to check if a number is a multiple of 7 or not

num=int(input("Enter the number: "))
if(num==1 or num==7 or num%7==0):
    print("The number is multiple of 7")
else:
    print("The number is not the multiple of 7")
