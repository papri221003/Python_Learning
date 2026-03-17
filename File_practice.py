with open ("Text.txt","r") as file:
    
    data=file.read()
    """
    num=""
    for val in range(len(data)):
        if(data[val]==","):
            if(int(num)%2==0):
                print("EVEN")
            else:
                print("ODD")
            num=""
        else:
            num+=data[val]    
    """
    
    new_data=data.split(",")
    
    for val in new_data:
        if(int(val)%2==0):
            print("EVEN")
        else:
            print("ODD")
            
    
    
    
    
    