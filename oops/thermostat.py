"""
Create a class called Thermostat to control room temperature.

1. Attributes in __init__:
room_name (string, e.g., "Living Room")
temperature (integer, e.g., default 24)

2. Methods to write:

increase_temp(): Adds 1 to temperature and prints the new temperature.
decrease_temp(): Subtracts 1 from temperature and prints the new temperature.
show_temp(): Prints: "Living Room temperature is currently 24°C".

"""


class Thermostat:
    # constructor
    def __init__(self, room_name, temp):
        self.room_name = room_name
        self.temp = temp

    # methods
    def increase_temp(self):
        self.temp = self.temp + 1
        print("temperature increased to", self.temp + 1)

    def decrease_temp(self):
        self.temp = self.temp - 1
        print("temperature increased to", self.temp)

    def show_temp(self):
        print("current temperature is", self.temp)


sectionA = Thermostat(room_name="section-a", temp=25)
# increase 1 time
sectionA.increase_temp()

# decrease 3 time
sectionA.decrease_temp()
sectionA.decrease_temp()
sectionA.decrease_temp()

# show temperature
sectionA.show_temp()
