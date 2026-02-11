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

def show_larger(num1, num2):
    if num1 > num2:
        diff = num1 - num2
        print(f'{num1} is larger than {num2} by {diff}')
    if num2 > num1:
        diff = num2 - num1
        print(f'{num2} is larger than {num1} by {diff}')
    if num1 == num2:
        print(f'The integers are equal, both are {num1}')

def main():
    numA = random.randint(1,5)
    numB = random.randint(1,5)
    show_larger(numA, numB)

if __name__ == '__main__':
    main()
    