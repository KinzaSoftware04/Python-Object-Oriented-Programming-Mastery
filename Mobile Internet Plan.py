class mobile_internet_plan:
    def __init__(self, name , data):
        self.name = name
        self.__balance= data
    def Internet_security(self , internet):
        if internet<0:
            print("Security Alert! Internet cannot be in minus.")
    def Internet_usage(self , gb_used):
        if gb_used <= self.__balance:
           self.__balance -= gb_used
           print(f"your remaining balance is:{self.__balance}") 
        if self.__balance == 0:
            print("Transection denied! your balance is not exists")
mobile = mobile_internet_plan("Kinza" , 20 )
print(mobile.name)
mobile.Internet_security(-5)
mobile.Internet_usage(20)




        