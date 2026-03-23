class Account:
    
    def __init__(self,acc_no,acc_pass):
        self.__acc_no=acc_no
        self.__acc_pass=acc_pass
        
    def pass_reset(self,new_pass):
        
        print("Old Password for the account no_",self.__acc_no,"is: ",self.__acc_pass)
        
        self.new_pass=new_pass
        print("New pass is: ",self.new_pass)
        
a1=Account(125478090,"Papri@22")

a1.pass_reset("teest12")