class Vehicle:
    def __init__(self , brand):
       
        self.brand = brand
    def __str__(self):
        return f"Vehicle brand {self.brand}"
class Car(Vehicle):
    def __init__(self , brand , roll_num):
        super().__init__(brand)
        self.roll_num = roll_num
    def __str__(self):
        return f" Car brand is: {self.brand} | Roll Num {self.roll_num}"
my_car = Car("toyota" , 101)
print(my_car)