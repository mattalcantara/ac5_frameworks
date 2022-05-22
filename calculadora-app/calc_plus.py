import math 
from math import *

def square(number_1):
    print(number_1)
    assert type(number_1) == int
    return number_1 ** 2

def power(number_1, number_2):
    print (number_1, number_2)
    assert type(number_1) == int 
    assert type(number_2) == int
    return pow(number_1, number_2) 

def logaritmo(number_1):
    print(number_1)
    assert type(number_1) == int 
    return math.log(number_1)
     