# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:38:55 2024

@author: Marcelo
"""

value = 20

for i in range(1, value + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        