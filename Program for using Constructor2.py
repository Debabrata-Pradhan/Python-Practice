#Program for using Constructor2
class Car:
    # 1. CONSTRUCTOR DEFINITION
    # The __init__ method acts as the constructor in Python
    def __init__(self, model_name, model_year):
        self.model = model_name   # Setting the initial values (attributes)
        self.year = model_year
        print("Constructor executed: Object created!")

    # Method to display car info
    def display_details(self):
        print(f"Car Model: {self.model}, Year: {self.year}")


# 2. CONSTRUCTOR CALL
# Calling the class name like a function triggers the __init__ constructor
my_car = Car("Tesla Model 3", 2026)

# Using the initialized object
my_car.display_details()
