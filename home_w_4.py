#  1 //
from sys import argv
name, first, second, third = argv
def calcul(first, second, third):
    return int(first) * int(second) + int(third)

print(" 1: Часы", first)
print(" 2: Ставка в час ", second)
print(" 3: Премия ", third)
print(" 4: Итого за рабочий период :", calcul(first, second, third))


# 2 //
my_list = [3,4,5,6,7,8,9,10]
print(my_list)
new_list =[el for el in my_list if el%2 == 0]
print(new_list)
# 3//
print([el for el in range(21,240,21)])
# 4 //
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)

new_list = []
for el in my_list:
    if el not in new_list:
        new_list.append(el)

print(new_list)
print([el for el in my_list and new_list])
# 5//
from functools import reduce
new_list = []
for el in range(100,1002,2):
    new_list.append(el)
print(reduce(lambda x,y: x+y,new_list))
# 6 //
from itertools import count
from itertools import cycle
for el in count(10,2):
    if el > 23:
        break
    else:
        print(el)

progr_lang = ["anna", "diana", "karina", "marina"]
t = 0
for el in cycle(progr_lang):
    if t > 10:
        break
    else:
        print(el)
        t += 1
# 7 //
from math import factorial

def generator():
    for el in (1,2,3,4,5):
        yield el
num = [el for el in generator()]
for el in num:
    print(factorial(el))
