# todo
"""
Create a class called SmartBulb to control room lighting.

Attributes in __init__:

room (string, e.g., "Classroom A")
brightness (integer, default starting at 100)

Methods to write:

dim(): Subtracts 10 from brightness . E.g. Prints: "Brightness dimmed to 70%".

brighten(): Adds 10 to brightness . E.g.Prints: "Brightness increased to 90%".

night_mode(): Instantly sets brightness to 10 and prints "Night mode ON (10% brightness)".

"""

# this is a single line comment
"""
this is line 1 comment
this is line 2 comment
"""


class SmartBulb:
    # constructor
    def __init__(self, room, brightness):
        self.room = room
        self.brightness = brightness

    # methods
    def dim(self, a):
        self.brightness = self.brightness - a
        print("light reduced to", self.brightness)

    def brighten(self, b):
        self.brightness = self.brightness + b
        print("light increased to", self.brightness)

    def night_mode(self):
        self.brightness = 10
        print("Night Mode on - brightness = 10")


sectionB = SmartBulb(room="Section-B", brightness=100)

# dim the light three times
sectionB.dim(10)  # 90
sectionB.dim(15)  # 75
sectionB.dim(25)  # 50


# toggle to night mode
sectionB.night_mode()  # 10

# brighten the light two times
sectionB.brighten(15)  # 20
sectionB.brighten(10)  # 30
