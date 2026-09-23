class Restaurant:
    def __init__(self, rest_name):
        self.rest_name = rest_name

    # parking the car
    def park_vehicle(self):
        # print "park the vehicle here"
        print("Welcome to", self.rest_name)
        print("park the vehicle here")

    # getting the Menu Card
    def get_menu_card(self):
        # TODO: print "your menu card is here"
        print("your menu card is here")

    # order a food
    def order_food(self, recipe_name):
        # TODO
        # get recipe name as argument  and print "your order for {recipe_name} is getting ready"
        print("your order for", recipe_name, "is getting ready")
        # call fill_water()
        self.__fill_water()
        # call get_ingredients()
        self.__get_ingredients()
        # call prepare_food()
        self.__prepare_food(recipe_name)

    def get_bill(self):
        # TODO
        # print "Your Bill Amount is Rs.200/-"
        print("Your Bill Amount is Rs.200/-")
        self.__clean_restaurant()

    def __clean_restaurant(self):
        # TODO: print "Cleaning Work in Progress"
        print("Cleaning work in progress")

    def __fill_water(self):
        # TODO: print "Serve Water at the Table"
        print("Serve Water at the Table")

    def __get_ingredients(self):
        # TODO: print "get the ingredients for {item_name}"
        print("get the ingredients")

    def __prepare_food(self, food_name):
        # TODO: print "cooking your food in 10 minutes"
        print("cooking your food in 10 minutes", food_name)


# object
sample = Restaurant("Leo Cafe")
sample.park_vehicle()
sample.get_menu_card()
sample.order_food("Ginger Tea")
# sample.__fill_water() # not possible
sample.get_bill()


# examples

# public -> make_food
# private -> __preparing_food


"""
park vehicle
get menu card

order_food -> argument
(private) fill_water
(private) get_ingredients
(private) prepare_food


get_bill
clean restaurant
"""
