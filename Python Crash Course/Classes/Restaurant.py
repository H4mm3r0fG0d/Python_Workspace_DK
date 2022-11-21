class Restaurant:
    # Section 9-1. Restaurant
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self, restaurant_name, cuisine_type):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"Restaurant specialty is {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("We're open for business!")

thai_restaurant = Restaurant("Sisters Cafe", "Thai")
#thai_restaurant.describe_restaurant(thai_restaurant.restaurant_name, thai_restaurant.cuisine_type)
#thai_restaurant.open_restaurant()
#print(thai_restaurant.restaurant_name)
#print(thai_restaurant.cuisine_type)
#print("\t")
# Section 9-2. Three Restaurants

italian_restaurant = Restaurant("Villagio Trattorio", "Italian")

#italian_restaurant.describe_restaurant(italian_restaurant.restaurant_name, italian_restaurant.cuisine_type)
#print("\t")
bbq_joint = Restaurant("Franklin Barbecue", "Texas-Style BBQ")

#bbq_joint.describe_restaurant(bbq_joint.restaurant_name, bbq_joint.cuisine_type)
#print("\t")

jamaican_spot = Restaurant("Ivan's Bar and Restaurant", "Jamaican/Caribbean")

#jamaican_spot.describe_restaurant(jamaican_spot.restaurant_name, jamaican_spot.cuisine_type)
#print("\t")

# Section 9-3. Users
class User:
    def __init__(self, first_name, last_name, user_dob, user_address, user_email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_dob = user_dob
        self.user_address = user_address
        self.user_email = user_email
    
    def describe_user(self):
        print(f"User name: {self.last_name.title()}, {self.first_name.title()}")
        print(f"User DOB: {self.user_dob}")
        print(f"User address: {self.user_address}")
        print(f"User e-mail address: {self.user_email}")

    def greet_user(self):
        print("\t")
        print(f"Greetings, {self.first_name.title()}, and welcome to the cybersphere.")

diego = User("diego", "kendall", "12/17/1992", "12345 Somewhere Dr, Anytown, USA 20349", "diegokendall@acme.com")
#diego.describe_user()
#diego.greet_user()
kevin = User("kevin", "federline", "06/09/1420", "69420 White Trash Lane, Dirtville, USA 69420", "kfed@douchenozzle.org")
#kevin.describe_user()
#kevin.greet_user()
skylar = User("skylar", "fitzgerald", "05/07/1999", "207143 Truelove Avenue, Hometown, USA 22030", "sfitzgerald@hotgirl.com")
#skylar.describe_user()
#skylar.greet_user()