#########################################################################################
# Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 

def arithmetic_mean_of_numbers():
    numbers = input("Enter numbers, which you want to know arithmetic value: ")
    numbers = numbers.split(",")
    numbers = tuple(map(int, numbers))
    print (sum(numbers) / len(numbers))

arithmetic_mean_of_numbers()

##########################################################################################
# Написати функцію, яка повертає абсолютне значення числа

def modul_number():
    user_number = int(input("Your value: "))
    print (f"Модуль числа {user_number} =",abs(user_number))

modul_number()


##########################################################################################

# Написати функцію, яка знаходить максимальне число з двох чисел, 
# а також в функції використати рядки документації DocStrings.

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
##########################################################################################

# Написати програму, яка обчислює площу прямокутника, трикутника та кола 
# (написати три функції для обчислення площі, 
# і викликати їх в головній програмі в залежності від вибору користувача)

import math


select_figure = input("""Which geometric figure area do you want to know?
1.Rectangle
2.Triangle
3.Circle
Enter number of answer: """)


def area_of_the_rectangle():
    """Function asks lenght two sides of rectangle and calculates area"""
    first_side = input("Enter the length of first side: ")
    second_side = input("Enter the length of second side: ")
    area_rectangle = float(first_side) * float(second_side)
    print(f"Area of rectangle is {area_rectangle}")
    
def area_of_the_triangle():
    """Function asks hight and base of triangle and calculates area"""
    hight_of_triangle = input("Enter the hight of triangle: ")
    base_of_triangle = input("Enter the base of triangle: ")
    area_triangle = (float(hight_of_triangle) * float(base_of_triangle)) * 0.5
    print(f"Area of triangle is {area_triangle}")

def area_of_the_circle():
    """Function asks radius of circle and calculates area"""
    radius_of_triangle = input("Enter the radius of circle: ")
    area_circle = round((pow(int(radius_of_triangle),2) * math.pi),3)
    print(f"Area of circle is {area_circle}")

def incorrect_answer():
    """Asks again, if you have input incorrect answer"""
    new_answer = input("Choose from 1 to 3, please: ")  
    if int(new_answer) == 1:
         area_of_the_rectangle()
    elif int(new_answer) == 2:
        area_of_the_triangle()
    elif int(new_answer) == 3: 
        area_of_the_circle()
    else:
        incorrect_answer()       


if int(select_figure) == 1:
    area_of_the_rectangle()
elif int(select_figure) == 2:
    area_of_the_triangle()
elif int(select_figure) == 3: 
    area_of_the_circle()
else:
    incorrect_answer()


##########################################################################################
