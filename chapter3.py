#LIST AND TUPLES
#WAP to ask the user to enter names of their 3 favorite movies & store then in a list
"""
list=[]
list.append(input("Enter the 1st movie name: "))
list.append(input("Enter the second movie name: "))
list.append(input("Enter the third movie name: "))

print(list)
print(len(list))


#Wap to check if the list contains element of palindrom sequence
list=[]
list.append(input("Enter the element: "))
list.append(input("Enter the element: "))
list.append(input("Enter the element: "))
list.append(input("Enter the element: "))
list.append(input("Enter the element: "))
listcpy=list.copy()
list.reverse()
if(listcpy==list):
    print("Palindrome")
else:
    print("Not Palindrome")
"""

#WAP to count "A" graded student in the following tuple
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
print(len(tup))

mylist=list(tup)

mylist.sort()
print(mylist)
mylist[0]="K"
print(mylist)