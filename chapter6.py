"""
#AVG of three numbers

def cal_avg(a,b,c):
    avg=(a+b+c)/3
    return avg

result1=cal_avg(1,2,3)
print(result1)


#WAF to print the elements of a list in a single line(List is the parameter)
def print_in_oneLine(list):
    for el in list:
        print(el,end=" ")
        
Places=["Konnagar","Rishra","Uttarpara","Hindmotor"]
print_in_oneLine(Places)

#WAF to find the factorial of n

def detect_factorial(n):
    fact=1
    while (n!=1):
        fact=fact*n
        n-=1
    return fact

print(detect_factorial(6))
        
#WAF to find even and ODD

def EVEN_ODD(num):
    if(num==0):
        print("EVEN")
    if(num==1):
        print("ODD")
    
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")
        
EVEN_ODD(99)    


#WAF to convert USD to INR

def convert_usd_inr(USD_val):
    inr_val=USD_val*95.56
    print("USD_VAL=",USD_val,"INR_VAL=",inr_val)
    

convert_usd_inr(2)

"""

#RECURSION

#print n to 1 in backwards

def show(n):
    if (n==0):
        return
    print(n)
    show(n-1) 
    
show(5)

#Factorial number using recursion

def fact(num):
    if(num==1 or num==0):
        return 1
    return num*fact(num-1)  

print(fact(5))  

#WAP to calculate first n natural numbers
def cal_sum(n):
    if(n==1):
        return 1
    return n+cal_sum(n-1)

print(cal_sum(10))

#WAP to print all elements in a list using recursive function

list=["A","B","C","D","E","F","G","H"]

def print_list(idx,list):
    if(idx==len(list)):
        return
    print(list[idx],end=" ")
    print_list(idx+1,list)
    
print_list(0,list)