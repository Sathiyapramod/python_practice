"""
Create a Vehicle class with a private attribute __speed.
Create methods to increase and decrease the speed.
Speed should never become negative.
"""

class Vehicle:
    # constructors
    def __init__(self, x):
        self.__speed = x

    # methods
    def increase_speed(self, inc):
        self.__speed = self.__speed + inc
        print("Speed increased to", self.__speed)

    def decrease_speed(self, dec):
        self.__speed = self.__speed - dec
        self.__make_horn()
        print("Speed decreased to", self.__speed)

    def __make_horn(self):
        print("car is honking")


punch = Vehicle(100)
punch.increase_speed(50)
punch.increase_speed(20)

punch.decrease_speed(90)
