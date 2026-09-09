"""
#print 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
    
print("\n")
#print 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
    
#Print multiplication table of number n
n=int(input("Enter the number for creating the table: "))
i=1
while i<=10:
    print(n*i)
    i+=1
"""
#print the elements of the following list using a loop

list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print(list[i])
    i+=1
print("\n")
    

for j in list:
    print(j)

#Searching
list=[4,5,8,13,16,25,29,30,45,50]
x=int(input("Enter the number in the list: "))

#using while loop
i=0
while i<len(list):
    if(list[i]==x):
        print(i)
        break
    else:
        i+=1
        
#using for loop
y=int(input("Enter the number in the list: "))
for el in range(0,len(list)):
    if(list[el]==y):
        print(el)
        break