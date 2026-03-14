#WAP to find the sum of first n numbers. (using while)

i=1
n=int(input("Enter the number: "))
sum=0
while(i<=n):
    sum=sum+i
    i+=1
print(sum)


#WAP to find the factorial of first n numbers. (using for)
m=int(input("Enter the number for determining its factorial: "))
fact=1
for idx in range(1,m+1):
    fact=fact*idx
    idx+=1
print(fact)

