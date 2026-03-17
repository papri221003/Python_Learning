def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))


#Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
    
print(sum(10))

"""
Write a recursive function to print all elements in a list.
Hint : use list & index as parameters.
"""

cities=["Mumbai","Kolkata","Noida","Chennai","Delhi","Gurgaon"]