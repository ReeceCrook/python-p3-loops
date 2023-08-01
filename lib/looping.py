#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i >= 0:
        if i == 0:
            i -= 1
            print("Happy New Year!")
        else:
            print(i)
            i -= 1

def square_integers(int_list):
    # code goes here!
    squared_list = [number * number for number in int_list]
    return squared_list

def fizzbuzz():
    # code goes here!
    for i in range(101):
        if i == 0:
            pass
        elif (i / 3).is_integer() and (i / 5).is_integer():
            print("FizzBuzz")
        elif (i / 3).is_integer():
            print("Fizz")
        elif (i / 5).is_integer():
            print("Buzz")
        else:
            print(i)
