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
thai_restaurant.describe_restaurant(thai_restaurant.restaurant_name, thai_restaurant.cuisine_type)
thai_restaurant.open_restaurant()
#print(thai_restaurant.restaurant_name)
#print(thai_restaurant.cuisine_type)
print("\t")
# Section 9-2. Three Restaurants

italian_restaurant = Restaurant("Villagio Trattorio", "Italian")

italian_restaurant.describe_restaurant(italian_restaurant.restaurant_name, italian_restaurant.cuisine_type)
print("\t")
bbq_joint = Restaurant("Franklin Barbecue", "Texas-Style BBQ")

bbq_joint.describe_restaurant(bbq_joint.restaurant_name, bbq_joint.cuisine_type)
print("\t")

jamaican_spot = Restaurant("Ivan's Bar and Restaurant", "Jamaican/Caribbean")

jamaican_spot.describe_restaurant(jamaican_spot.restaurant_name, jamaican_spot.cuisine_type)
print("\t")

# Section 9-3. Users
