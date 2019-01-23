# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

my_list = [26, 54, 93, 17, 77, 31, 44, 55, 20]

for x  in range(0, len(my_list)):
    for y in range(0, len(my_list)-1):
        if my_list[y] > my_list[y+1]:
            temp = my_list[y]
            my_list[y] = my_list[y+1]
            my_list[y+1] = temp
print(my_list)









