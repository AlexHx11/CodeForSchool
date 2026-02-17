# Alex Ha
# 2543681
# COP1000

# collaborator: none

"""
Pseudocode 

Loop 4 times
    Loop 3 times
        if iteration is the first or last
            display "0123456789"
        else
            loop 8 times
                display "0         9"

"""

# Program 

# Loops 4 shapes
for num_of_shapes in range(0,4):
    # Checks if printing top and bottom or empty middle rows
    for iteration in range(0,3):
        # Prints top and bottom
        if iteration == 0 or iteration == 2:
            print("0123456789")
        # Prints middle section
        else:
            for empty_rows in range(0,8):
                print("0        9")

                