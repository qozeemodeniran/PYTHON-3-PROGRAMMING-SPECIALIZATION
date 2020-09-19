# -*- coding: utf-8 -*-
import copy
names = [['students', ['Qozeem', 'Taofik']], ['departments', ['Computer Scienc', 
         'Public Administration']]]
shallow_copy_version = names[:]
deeply_copied_version = copy.deepcopy(names)
names.append('Grades')
names[0].append('Segun')
print('---NAMES---')
print()
print(names)
print('---DEEP COPY---')
print()
print(deeply_copied_version)
print('---SHALLOW COPY---')
print()
print(shallow_copy_version)

