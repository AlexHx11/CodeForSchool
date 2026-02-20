# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode 

Create an empty list
Loop 12 times:
    Add a random number from 50-100 to the list.
Loop over the list:
    Print out each element on the same line.
Display the element at index 3, 9, and the smallest with the (min) function.
Use the change_list function that'll be specified below.
Assigned the new list to a new variable
Loop and display the new list


Create a list from change_list
    Pull out the middle 6 elements (3:10)
    Define length
    Loop through the list
        Add 1 to length for each item in the list.
    print out the length
    Sort the list using the sort method
    Return the list.

"""
import random

def main():

    # Creates a new list with 12 random integers
    list = []
    for i in range(12):
        list.append(random.randint(50, 100))

    # Displays the list and the 4th, index 9, and smallest number
    print("Here is the list of random integers...")
    for num in list:
        print(f"{num}", end=" ")
    print("\n", end="")

    print(f"The 4th element in the list is {list[3]}")
    print(f"The element at index 9 is {list[9]}")
    print(f"The smallest element in the list is {min(list)}")

    # Use the change list function and displays it
    new_list = change_list(list)
    print("change_list returned this sorted list...")
    for num in new_list:
        print(f"{num}", end=" ")
    print("\n", end="")


def change_list(list):

    # Splices the list
    new_list = list[3:9]

    # Measures the list length
    length = 0
    for len in new_list:
        length += 1
    print(f"The size of the list is now {length}")

    # Sort and return the list
    new_list.sort()
    return new_list


if __name__ == '__main__':
    main()