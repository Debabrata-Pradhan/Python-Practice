#Program for using Constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Tesla", "Model 3")

print(my_car.brand)
