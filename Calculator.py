FirstNum=int(input("Enter the Fist Number:"))
operator=input("Enter the operator(+,-,/,*,%): ")
SecondNum=int(input("Enter the Second Number:"))

if (operator=='+'):
    print("The answer is: ",FirstNum+SecondNum)
elif(operator=='-'):
    print("The answer is: ",FirstNum-SecondNum)
elif(operator=='/'):
    print("The answer is: ",FirstNum/SecondNum)
elif(operator=='*'):
    print("The answer is: ",FirstNum*SecondNum)
elif(operator=='%'):
    print("The answer is: ",FirstNum%SecondNum)
    
else:
    print("INCORRECT!!!")