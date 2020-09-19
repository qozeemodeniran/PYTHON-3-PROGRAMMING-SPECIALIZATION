# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 01:18:16 2020

@author: Odeniran Qozeem
"""

nested1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']] #Creates a list with three items

print(nested1[0]) #Prints the item in posistion 1

print(len(nested1)) #Prints the length of nested1

nested1.append(['x', 'y', 'z']) #Adds a list of "x,y,z" to nested1

for l in nested1: #iterates through the new nested1 list
    print(l) #prints all items of the new nested1 list
    
print('\n*****************************************************************************')

y = nested1[1] #Saves ['d', 'e'] into a variable y
print(y) 
print(y[0])

print('\n******************************************************************************')

print([10, 20, 30][1]) 
"""The first []  is used to create a list with 10, 20, 30.
The second [] is used to output the item  in index 1 which is 20 """

print('\n*******************************************************************************')
nested1[1] = [1, 2, 3] #Changes d,e to 1,2,3
nested1[1][0] = 100 #Changes 1 to 100
print(nested1)

print('\n********************************************************************************')
nested2 = [{'a':1, 'b':3}, {'a':5, 'c':90, 5:50}, {'b':3, 'c':"yes"} ] #list of dictionaries
print(nested2)
print(type(nested2))