#task2.1
import numpy  

some_numbers = 7549

get_list = list(map(int,str(some_numbers)))
print (numpy.prod(get_list))

#task2.2
get_list.reverse()
print (get_list)

#task2.3
get_list.sort()
print (get_list)
