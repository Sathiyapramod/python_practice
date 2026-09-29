# parent class
class Animal:
    # constructor
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def show_color(self):
        pass

    def get_name(self):
        print("Animal name is", self.animal_name)


# child class
class Dog(Animal):
    # constructor
    def __init__(self, dog_name):
        super().__init__(animal_name=dog_name)

    def show_color(self):
        print("I am Brown")


class Cow(Animal):
    # constructor
    def __init__(self, cow_name):
        super().__init__(animal_name=cow_name)

    def show_color(self):
        print("I am Black")


cooper = Dog("cooper")
cooper.show_color()
cooper.get_name()

cow = Cow("test")
cow.show_color()
cow.get_name()
