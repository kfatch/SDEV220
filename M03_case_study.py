#Kody Fatch
#Module 3 Case Study: Lists, Functions, and Classes
#This program will take information from input about a user's vehicle. Next, the program will output the info in a neat, formatted way.

class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def vehicle_info(self):
        print(f"Vehicle type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

vehicle_type = input("Enter the type of your vehicle:\n")
vehicle_year = int(input("Enter the year of your vehicle:\n"))
while (vehicle_year < 1900) or (vehicle_year > 2026):
    vehicle_year = int(input("Enter a valid year.\n"))
vehicle_make = input("Enter the make of your vehicle:\n")
vehicle_model = input("Enter the model of your vehicle:\n")
num_doors = int(input("Does your vehicle has 2 or 4 doors?\n"))
while (num_doors < 2) or (num_doors > 4) or (num_doors == 3):
    num_doors = int(input("Enter a valid number of doors.\n"))
roof_type = int(input("Is your vehicle's roof a soft-top (Select 1), hard-top (Select 2), or a sun roof (Select 3)?\n"))
while (roof_type < 1) or (roof_type > 3):
    roof_type = int(input("Enter a valid option for your vehicle's roof type.\n"))
if roof_type == 1:
    roof_type = "Soft-top"
elif roof_type == 2:
    roof_type = "Hard-top"
elif roof_type == 3:
    roof_type = "Sun roof"

my_vehicle = Automobile(vehicle_type, vehicle_year, vehicle_make, vehicle_model, num_doors, roof_type)
my_vehicle.vehicle_info()