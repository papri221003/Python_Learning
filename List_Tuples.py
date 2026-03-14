#WAP to the user to give the movie names and store them in the list
"""
movie=[]
movie.append(input("Enter the movie name: "))
movie.append(input("Enter the movie name: "))
movie.append(input("Enter the movie name: "))

print(movie)

"""

#WAP to check if the list contains the elements they are pallindrome or not

list=[1,2,2,1]

list2=list.copy()
list2.reverse()

if(list==list2):
    print("Palindrome")
else:
    print("Not a Palindrome")
    

#WAP to count the number of students of grade A

student=("A","A","C","B","D","B")
print("'A' Graded students are: ",student.count("A"))
print("'B' Graded students are: ",student.count("B"))
print("'C' Graded students are: ",student.count("C"))

List_Student=["A","A","C","B","D","B"]
List_Student.sort()
print(List_Student)