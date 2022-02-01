

# class vs an instance of that class
# if you change an instance it doesn't effect the class itself
# an instance is a specific type within that class

# OOP


class Car:
    runs = True

    def start(self):
        if self.runs:
            print("--- Car is started. Vroom vroom!")
        else:
            print("--- Car is broken :(")

my_car = Car()
print(f"--- My car runs: {my_car.runs}")
my_car.start()