"""
Print the elements of the following list using a for loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
"""
list1=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for nums in list1:
    print(nums)
else:
    print("END")    




""" 
Search for a number x in this tuple using for loop:

[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

"""
tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=int(input("Enter the number: "))
idx=0;
for num in tuple:
    if(num ==x):
        print("Number found! at ",idx)
        break
    else:
        idx+=1
