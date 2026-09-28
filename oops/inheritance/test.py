# parent class
class Factory:
    # constructors
    def __init__(self, factory_name):
        self.factory_name = factory_name  # attributes

    # methods
    def open_factory(self):
        # !! Opening the Factory
        print("The Factory is open now")

    def make_automobile(self):
        pass

    def close_factory(self):
        # !! Closing the Factory
        print("The Factory is closed now")


# Bike Factory
class BikeFactory(Factory):
    # constructor
    def __init__(self, name):
        
        # this will allow to use the attributes from the parent class
        super().__init__(factory_name=name)  # "Royal Enfield"

    # methods
    # todo - I want to change here

    def make_automobile(self):
        print("Our Factory name is", " We are making bikes")

    def display_factory_name(self):
        print("My Factory Name is", self.factory_name)


# child class
test = BikeFactory("Royal Enfield")

test.open_factory()
# test.make_automobile()
test.display_factory_name()
test.close_factory()


"""
# Car Factory
class CarFactory(Factory):
    # constructors
    def __init__(self, name):
        self.name = name

    # methods
    # todo - I want to change here

    def make_automobile(self):
        print("our factory name is", self.name, "we are making cars")


print("________________________________________")
suzuki = CarFactory("suzuki")

suzuki.open_factory()
suzuki.make_automobile()
suzuki.close_factory()


class TruckFactory(Factory):
    # constructors
    def __init__(self, name):
        self.name = name

    # methods
    # todo - I want to change here

    def make_automobile(self):
        print("our factory name is", self.name, "we are making trucks")


print("________________________________________")
volvo = TruckFactory("volvo")

volvo.open_factory()
volvo.make_automobile()
volvo.close_factory()
"""
