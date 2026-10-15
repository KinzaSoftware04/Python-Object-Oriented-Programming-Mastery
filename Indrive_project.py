class Vehicle:
    def __init__(self , brand):
        self.brand = brand
    def __str__(self):
        return f"Car brand is: {self.brand}"
class Bike(Vehicle):
    def __init__(self , brand , fare_rate):
        super().__init__(brand)
        self.fare_rate = fare_rate
    def __str__(self):
        return super().__str__() + f" Bike Rent on kilometers is {self.fare_rate }"    
my_vehicle = Vehicle("Honda")
my_bike =  Bike("Toyota" , 200)

print(isinstance(my_bike , Vehicle))
print(issubclass(Bike , Vehicle))
print(my_bike)
print(my_vehicle)
