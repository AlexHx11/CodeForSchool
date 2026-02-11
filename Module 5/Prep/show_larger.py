# Alex Ha
# 2543681
# COP1000

"""
Psuedocode 

Define a function that takes two numbers as parameters
The function compares the two numbers
If the first number is larger than the second
    subtract (-) the first number by the second and save it as the difference 
    display that the first is larger and its difference 
If the second number is larger than the first
    subtract (-) the second number by the first and save it as the difference 
    display that the second is larger and its difference 
If both numbers are equal
    display that both numbers are equal

Check that the function ISN'T imported by seeing if the name of the program is main

"""
import random

def show_larger(num_1, num_2):
    if num_1 > num_2:
        diff = num_1 - num_2
        print(f'{num_1} is larger than {num_2} by {diff}')
    if num_2 > num_1:
        diff = num_2 - num_1
        print(f'{num_2} is larger than {num_1} by {diff}')
    if num_1 == num_2:
        print(f'The integers are equal, both are {num_1}')

def main():
    num_A = random.randint(1,5)
    num_B = random.randint(1,5)
    show_larger(num_A, num_B)

if __name__ == '__main__':
    main()
