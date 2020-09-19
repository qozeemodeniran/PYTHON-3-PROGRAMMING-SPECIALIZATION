# -*- coding: utf-8 -*-
def double(a_list):
    new_list = []
    for value in a_list:
        new_elem = value * 2
        new_list.append(new_elem)
    return new_list

numbers = [2, 3, 1]
print(numbers)
print()
numbers = double(numbers)
print(numbers) 


