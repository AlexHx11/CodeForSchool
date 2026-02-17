# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode

Import the math module

Define a function that calculates surface area, taking the length, width, and height as inputs
    Return the surface area by multiplying the length by the width by 2, adding that to the product of the width and height and 2, and adding that to the product of the length and height by 2

Define a function that calculates the diagonal, taking the length, width, and height as inputs
    Return the diagonal by getting the square root of the whole following: length squared plus width squared plus height squared

Define a function that displays the volume, taking the length, width, and height as inputs
    Multiply all the dimensions and save it as volume
    Display the volume 

Define a main function where the core program runs
    Prompt the user to enter a length as a float
    Prompt the user to enter a width as a float
    Prompt the user to enter a height as a float

    Display the surface area by calling the surface area function with length, width and height as arguments
    Display the diagnoal by calling the diagonal function with length, width and height as arguments
    Call the volume function with length, width and height as parameters

Check and make sure the execution is called main then run main

"""

import math

# Geometric functions
def get_surface_area(length, width, height) :
    surface_area = (2 * length * width) + (2 * length * height) + (2 * height * width)
    return surface_area

def get_diagonal(length, width, height) :
    diagonal = math.sqrt(length**2 + width**2 + height**2)
    return diagonal

def print_volume(length, width, height) :
    print(f"The volume of the rectangular cuboid is {(volume := length * width * height):.3f}")

def main():
    # Inputs for dimensions
    length = float(input("Enter the length of the rectangular cuboid: "))
    width = float(input("Enter the width of the rectangular cuboid: "))
    height = float(input("Enter the height of the rectangular cuboid: "))

    # Gets and prints each calculation (except volume which prints itself)
    print(f"The surface area of the rectangular cuboid is {(surface_area := get_surface_area(length, width, height)):.4f}")
    print(f"The diagonal of the rectangular cuboid is {(diagonal := get_diagonal(length, width, height)):.3f}")
    print_volume(length, width, height)

if __name__ == '__main__' :
    main()