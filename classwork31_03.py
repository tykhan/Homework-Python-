###############################################################################
# В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

for x in range(1,11):
    if x % 2 == 0:
        print(f"{x} ділиться націло на 2")
    if x % 3 == 0:
        print(f"{x} ділиться націло на 3")
    if x % 3 != 0 and x % 2 != 0:
        print(f"{x} не ділиться націло на 2 і 3")

###############################################################################
# Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

login_name = input("Your login: ")

while login_name != "First":
    login_name = input("Incorrect. Try again: ")
    continue
else:
    print("Success!")


###############################################################################
# Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. 
# При появі від’ємного числа програма зупиняється 
# (якщо зустрічається 0 програма теж зупиняється).

user_number = (input("Введіть число: "))
while int(user_number) >= 0:
    print (f"{user_number} - додатнє число. Введіть інше число.")
    user_number = (input("Інше число: "))
    while int(user_number) == 0:
         user_number = input("Ще трішки менше: ")
else:
    print("Ви ввели від'ємне число")

###############################################################################

#  Створити список цілих чисел, які вводяться з терміналу 
#  та визначити серед них максимальне та мінімальне число.

some_list = []
amount_of_numbers = int(input("How much numbers will be in your list?: "))

for x in range(amount_of_numbers):
    user_number = int(input("Value: "))
    some_list.append(user_number)
print(f"Maximal number in your list is: {max(some_list)}")
print(f"Minamal number in your list is: {min(some_list)}")

     

###############################################################################


###############################################################################
