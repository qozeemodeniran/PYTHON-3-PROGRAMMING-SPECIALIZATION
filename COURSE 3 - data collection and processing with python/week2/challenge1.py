# -*- coding: utf-8 -*-
"""
1. Using map, create a list assigned to the variable greeting_doubled 
that doubles each element in the list lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

"""
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def transformer(big):
    return 2 * big

greeting_doubled = map(transformer, lst)

print(greeting_doubled)
    
