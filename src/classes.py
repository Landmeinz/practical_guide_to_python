

# class vs an instance of that class
# if you change an instance it doesn't effect the class itself
# an instance is a specific type within that class

# OOP


# class Car:
#     runs = True
#     # self keyword used for the instance of the class
#     def start(self):
#         if self.runs:
#             print("--- Car is started. Vroom vroom!")
#         else:
#             print("--- Car is broken :(")

# my_car = Car()
# my_car.runs = False
# print(f"--- My car runs: {my_car.runs}")
# my_car.start()

# my_other_car = Car()
# # dont need to define if the car runs as that's the default defined above in the class
# print(f"--- My car runs: {my_other_car.runs}")
# my_other_car.start()


# Car.start(); this wont work; it's expecting an instance and not a class

type(42)
type("hi")

print(isinstance(42, int))
print(isinstance("hi", str))
print(isinstance("hi", int))

# print(isinstance(my_other_car, Car))  # returns True


# class Car:
#     runs = True

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start(self):
#         if self.runs:
#             print(f"Your {self.make} {self.model} is started. Vroom vroom!")
#         else:
#             print(f"Your {self.make} {self.model} is broken")


# my_car = Car("Ford", "Thunderbird")
# my_car.start()

# __str__ and __repr___   -   good for debugging

import datetime
now = datetime.datetime.now()
print(str(now))

print(repr(now))

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

my_car = Car("Ford", "Thunderbird")
print(f"This object is a {str(my_car)}")
print(f"To reproduce it, type: {repr(my_car)}")