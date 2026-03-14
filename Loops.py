"""  
#Wap to write all numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#Wap to write all numbers from 100 to 1  

j=100
while j>=1:
    print(j)
    j-=1  
""" 
#Wap to print the multiplication table for number n

n=int(input("Enter the number: "))
i=0
while i<=10:
    print(i*n)
    i+=1


#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list1=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

i=0
while i<len(list1):
    print(list1[i])
    i+=1
    
""" 
Search for a number x in this tuple using loop:

[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
"""

tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100,9)

x=int(input("Enter the number to be searched: "))
a=0
while (a<len(tuple)):
    if (tuple[a]==x):
        print("The searched number is in: ",a)
        
    else:
        print("Finding...")
    a+=1


