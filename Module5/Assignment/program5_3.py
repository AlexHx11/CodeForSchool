# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode 

Import program5_2.py and save it as geometry

Define a main function where the core program runs
    Prompt the user to enter a length as a float
    Prompt the user to enter a width as a float
    Prompt the user to enter a height as a float

    Display the surface area by calling the surface area function with length, width and height as arguments
    Display the diagnoal by calling the diagonal function with length, width and height as arguments
    Call the volume function with length, width and height as parameters

Check and make sure the execution is called main then run main

"""
# Import functions as geometry
import program5_2 as geometry

def main():
    # Inputs for dimensions
    length = float(input("Enter the length of the rectangular cuboid: "))
    width = float(input("Enter the width of the rectangular cuboid: "))
    height = float(input("Enter the height of the rectangular cuboid: "))

    # Gets and prints each calculation (except volume which prints itself)
    print(f"The surface area of the rectangular cuboid is {(surface_area := geometry.get_surface_area(length, width, height)):.4f}")
    print(f"The diagonal of the rectangular cuboid is {(diagonal := geometry.get_diagonal(length, width, height)):.3f}")
    geometry.print_volume(length, width, height)

if __name__ == '__main__' :
    main()