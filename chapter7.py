f=open("Practice.txt","w")

f.write("Hi EveryOne.\nWe are learning I/O using java.\nI like Programming in java.")

#Replace java with python
with open("Practice.txt","r") as f1:
    new_data=f1.read()
    new_data.replace("java","Python")
    
with open("Practice.txt","w") as f2:
    f2.write(new_data)


