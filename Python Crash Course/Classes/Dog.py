class Dog:
    # A simple attempt to model a dog.

    def __init__(self, name, age):
        # Initializing the name and age attributes.
        self.name = name
        self.age = age

    def sit(self):
        # Simulates the dog sitting in response to a command.
        print(f"{self.name}, sit!")
        print("...")
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # Simulates the dog sitting in response to a command.
        print('"Now roll over!"')
        print("...")
        print(f"{self.name} rolled over!")

dk_dog = Dog('Bastion', 12)

print(f"My dog's name is {dk_dog.name}.")
print(f"My dog is {dk_dog.age} years old.")
print("\t")
dk_dog.sit()
print("\t")
#dk_dog.roll_over()

sky_dog = Dog('Kota Ri', 5)

print(f"Your dog's name is {sky_dog.name}.")
print(f"Your dog is {sky_dog.age} years old.")
print("\t")
sky_dog.sit()
