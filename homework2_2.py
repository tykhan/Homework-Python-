#task2.1
import numpy  

some_numbers = 7549

get_list = list(map(int,str(some_numbers)))  #перетворюєм int into list
print ("Добуток чисел 7549 =", numpy.prod(get_list))

#task2.2
get_list.reverse()
print ("Числа 7549 в реверсному порядку -", get_list)

#task2.3
get_list.sort()
print ("Числа 7549 в порядку зростання -", get_list)
