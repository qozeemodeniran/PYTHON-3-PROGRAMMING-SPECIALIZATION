# -*- coding: utf-8 -*-
names = [['Qozeem', 'Taofik'], ['Odeniran', 'Bankole']]
copied_outer_list = []
for inner_list in names:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list) #poduces the names list.
print()
print()
names[0].append(['Segun'])
print(names) #adds 'segun' to the first part of names[]
print()
print()
print(copied_outer_list)

