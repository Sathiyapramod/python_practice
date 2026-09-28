# parent class


class Factory:
    # constructors
    def __init__(self):
        pass

    # methods
    def open_factory(self):
        print("The Factory is open now")

    def make_automobile(self):
        print("We are making something")

    def close_factory(self):
        print("The Factory is closed now")


# create your child class
# call your parent class as parameter


class BikeFactory(Factory):
    # constructor
    def __init__(self, name):
        self.name = name
        pass

    # methods
    def make_bikes(self):
        print("Our Factory name is", self.name, " We are making bikes")


# child class
test = BikeFactory("Royal Enfield")

# calling my parent class method
# start the factory
test.open_factory()

# making the bikes
test.make_bikes()
test.make_automobile()

# close the factory
test.close_factory()
