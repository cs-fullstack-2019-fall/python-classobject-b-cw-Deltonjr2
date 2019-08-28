# python-classObject_b-cw
# Start with a main function and make each problem a function. Call those functions from your main function.
#
# Problem 1:
#
# Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class. Create an object of Dog in your problem1 function and print all of it's attributes.
#
# Problem 2:
#
# We will keep having this problem until EVERYONE gets it right without help
#
# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
#
# Problem 3:
#
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have several functions:
#
# a) One function that can change the name of the product.
#
#     b) Another function that can change the name and price of the product.
#
#     c) A last function that can change the name, price, and quantity of the product.
#
#     Create an object of Product and print all of it's attributes.

# # 1. # Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class. Create an object of Dog in your problem1 function and print all of it's attributes.
#
# class Dog:
#     def __init__(self, name, breed, color, gender):
# # my properties
#         self.name=name
#         self.breed=breed
#         self.color=color
#         self.gender=gender
#
#     def ShowmyWork(self):
#
#         print(f"{self.name}, {self.breed}, {self.color},{self.gender}")
#
# def problem1():
#     dogOption1= Dog("fido","bulldog", "black", "male")
#     dogOption1.ShowmyWork()
#
# problem1()
#
# # //2. Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
#
# userInput = ""
# while(userInput != "="):
#     userInput = input("Enter another string")

//3. # Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have several functions:
#
# a) One function that can change the name of the product.
#     b) Another function that can change the name and price of the product.
#
#     c) A last function that can change the name, price, and quantity of the product.
#
#     Create an object of Product and print all of it's attributes.

class Plasticplates():

def __init__(self, name , quantity, price):

        self.name=name
    self.price=price
        self.quantity=quantity

 def mywork(self):
     print(f"{self.name}, {self.price}, {self.quantity},")

def problem1():
    online1 = Plasticplates ("200","$80")
    online1.printmywork()
