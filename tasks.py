# SMART Targets.

# Task 1:
# Create a variable and assign it the value of “hello”
# Use an if statement to check if the variable is equal to hello, and if it is print”Hey there!”

greeting = "hello"
if greeting == "hello":
    print("Hey there!")

# Create a dictionary with the keys of “brand” with the value of “nike” and the key of “type” and the value of “shoe”.
# Access and print out the value held under type from the dictionary just created
shoe_dictionary = {
    "brand": "nike", 
    "type": "shoe"
    }

print(shoe_dictionary["type"])
#-------------------------------------------------------


# Task 2:
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
# Using a loop add two to each number
for i in range(len(numbers)):
    numbers[i] += 2

# Using a loop print out each number in the list
for number in numbers:
    print(number)


# Task 3:
# Create a person class with the properties of  name (str), wallet (int). And a  shopping list (List) that starts off empty
class Person:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.shopping_list = []


# Write  methods to add and remove items from the shopping list

    def add_item_to_list(self, shopping_list_item):
        self.shopping_list.append(shopping_list_item)
        

    def remove_item_from_list(self, shopping_list_item):
        self.shopping_list.remove(shopping_list_item)


# Write a method called `print_shopping_list` to print out each item in the shopping list (using a loop)
    def print_shopping_list(self):
        for shopping_list_item in self.shopping_list:
            print(shopping_list_item)

# Task 4:
# Create an instance of the person class
person_1 = Person("Wanda", 100)

# Add a string of “banana” to the shopping list of that person
person_1.add_item_to_list("banana")

# Add a string of “soap” to the shopping list of that person
person_1.add_item_to_list("soap")
# Print out the ‘name’ property of the person
print(person_1.name)
# Call the person’s method to print out the shopping list.
print(person_1.shopping_list)
# Task 5 :
# Try the lab with scaffold as a homework



