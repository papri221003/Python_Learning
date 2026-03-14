
"""
movie=[]
movie.append(input("Enter the movie name: "))
movie.append(input("Enter the movie name: "))
movie.append(input("Enter the movie name: "))

print(movie)

"""



# Palindrome list check
nums = [1,2,2,1]

nums2 = nums.copy()
nums2.reverse()

if nums == nums2:
    print("Palindrome")
else:
    print("Not a Palindrome")


# Count grades
student = ("A","A","C","B","D","B")

print("A grade:", student.count("A"))
print("B grade:", student.count("B"))
print("C grade:", student.count("C"))


# Sort list
list_student = ["A","A","C","B","D","B"]
list_student.sort()

print(list_student)