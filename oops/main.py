"""
SuperHero -> DEFINE CLASS

-> what is their name (print)
-> what is their power (showcase)
-> How much they have power (print)
-> increase / decrease their power (math calculation)
-> show their entire profile ()
"""

# hero name -> Spiderman
# Power Units -> (1000)

# actual name - Peter parker
# Strength -> College student & hero


class SuperHero:
    # constructor
    def __init__(self, hero_name, power):
        print("hero name is", hero_name)
        print("Their power is ", power)

        # create one instance inside the class
        self.my_hero = hero_name
        self.my_power = power
        print(self)

    # methods
    # print name
    def print_name(self):
        print(self.my_hero)

    # power quantity print
    def power_qty(self):
        print(self.my_power)


# create a new object
my_hero = SuperHero("Spider man", 1000)
