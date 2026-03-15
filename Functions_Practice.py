#WAF to print the length of a list. ( list is the parameter)
cities=["Mumbai","Kolkata","Noida","Chennai","Delhi","Gurgaon"]

def length_list(list):
    return(len(list))

length=length_list(cities)
print(length)

#WAF to print the elements of a list in a single line. ( list is the parameter)
def print_list_SingleLine(list):
    idx=0
    while (idx<length):
        print(list[idx],end=" ")
        idx+=1
    print("\n")
        
print_list_SingleLine(cities)



#WAF to find the factorial of n. (n is the parameter)
def factorial(n):
    idx=1
    fact=1
    while(idx<=n):
        fact=fact*idx
        idx+=1
    return fact    

result=factorial(5)
print(result)


#WAF to convert USD to INR.

def convert(usd):
    inr=usd*92.58
    return inr

amount=convert(10)
print(amount)