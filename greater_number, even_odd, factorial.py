##################################################################################

first_value = int(input("Enter your first value: "))
second_value = int(input("Enter your second value: "))

def greater_number():
    """Function calculates, what number is greater from two inputed values"""
    if first_value > second_value:
        print(f"Number {first_value} is greater than number {second_value}")
    elif first_value == second_value:
        print(f"Number {first_value} is equal with number {second_value}")
    else:
        print(f"Number {second_value} is greater than number {first_value}")
greater_number()

###################################################################################

user_number = int(input("Your value: "))

if user_number % 2 == 0:
    print("Your value is even")
else:
    print("Your value is odd")

###################################################################################

user_number = int(input("Enter your value: "))
a = 1
for i in range(1, user_number + 1):
    a *= i
print("Factorial of your number is: ", a)