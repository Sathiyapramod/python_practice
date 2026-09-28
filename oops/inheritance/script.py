# parent class
class Factory:
    # constructors
    def __init__(self):
        pass  # attributes

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
        self.name = name
        pass

    # methods
    # todo - I want to change here

    def make_automobile(self):
        print("Our Factory name is", self.name, " We are making bikes")


# child class
test = BikeFactory("Royal Enfield")

test.open_factory()
test.make_automobile()
test.close_factory()


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
