#################################################################################

import math


action = int(input("""What do you want to do with numbers
1. Addition
2. Subtraction
3. Multiplication
4. Division
Input, please: """))


def addition():
    list_with_numbers = []
    amount_of_numbber = int(input("How much numbers do you want to add: "))
    for x in range(amount_of_numbber):
        users_numbers = int(input("Enter value: "))
        list_with_numbers.append(users_numbers)      
    print("Sum of this numbers is", sum(list_with_numbers))

def subtraction():
    first_value = int(input("First value: "))
    second_value = int(input("Second value: "))
    print("Subtraction result of this numbers is", first_value - second_value)


def multiplication():
    list_with_numbers = []
    amount_of_numbber = int(input("How much numbers do you want to multiply: "))
    for x in range(amount_of_numbber):
        users_numbers = int(input("Enter value: "))
        list_with_numbers.append(users_numbers)      
    print("Result of multiplication of this numbers is", math.prod(list_with_numbers))

def division():
    first_value = int(input("First value: "))
    second_value = int(input("Second value: "))
    print("Division result of this numbers is", first_value / second_value)

if action == 1:
    addition()
if action == 2:
    subtraction()
if action == 3:
    multiplication()
if action == 4:
    division()

#################################################################################

import random

random_value = random.randint(1,100)
user_value = int(input("Your value?: "))

while user_value != random_value:
    if user_value > random_value:
        user_value = (int(input("Go down: ")))
        continue
    elif user_value < random_value:
        user_value = (int(input("Try bigger: ")))
        continue
    
if user_value == random_value:
    print("You win")        


#################################################################################