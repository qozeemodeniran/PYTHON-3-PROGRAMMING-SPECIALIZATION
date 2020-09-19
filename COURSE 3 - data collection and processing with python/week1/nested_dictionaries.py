
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:19:38 2020

@author: Odeniran Qozeem
"""
#TASK- extract the value associated with color an assign it to var color. Do not hardcode!
info = {'Personal_data':
        {'name': 'Qozeem',
         'age': 26,
         'major': 'Information and Commmunication Science',
         'physical_feature': 
             {'color': {'eye': 'black',
                        'hair': 'black'},
                'height': "5'8",}
    },
    'other':
        {'favourite_colors': ['yellow', 'white', 'red'],
         'interests': ['programming', 'reading', 'music']
         }
        }
        
print(info)

print('\n')

print(info['Personal_data'])

print('\n')

print(info['Personal_data']['physical_feature'])

print('\n')

color = info['Personal_data']['physical_feature']['color']
print(color)

print('\n')
print("The value associated with color is...")
for key, value in color.items():
    print(key.upper(), ' : ', value.upper())


    






























