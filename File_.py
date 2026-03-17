"""
with open ("Practice.txt","w") as f:
    f.write("Hi.Everyone.\nWe are learning file I/O")
    f.write("using Java\nI like Programming in Java")

"""

word="learning" 
def found():   
    with open ("Practice.txt","r+") as f:
        if(data.find(word)!=-1):
            print("Found!!")
        else:
            print("Not Found!")
            
with open ("Practice.txt","r+") as f:
    data=f.read()
    new_data=data.replace("Java","Python")
    
    data=new_data
    print(data)
    
found()
 
    

    


