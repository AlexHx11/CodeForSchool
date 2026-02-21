# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode 

Create a list with 64 elements with ages range 0-200

Pass it into a function that sorts the list in descending order and returns the new list

Define a current position
Loop 8 times
    Loop 8 times
        display each number at the current position inline
        increase the current position by one
    start a new line

Use the sum function to sum the list and display the sum
Determine the oldest and youngest in the list from the min and max functions
Use the sum from earlier, divide that by the count of items in the list to find the average
Use count to return the amount of trees less than or equal to 2 and return that number
Use list comprehension to create a list of all the ages between 3-20 then use count to display the amount
Do the same for ages 21-50
Do the same for ages 51-100
Do the same for ages 101+

"""

# Program
import random


def main():
    # Create the age list
    tree_ages = [random.randint(0,200) for tree in range(64)]

    # Sort the list (Descending)
    tree_ages = sort_descending(tree_ages)

    # Create the grid
    curr_index = 0
    for row in range(8):
        for item in range(8):
            print(f'{tree_ages[curr_index]:<4}', end='')
            curr_index += 1
        print('\n', end='')

    # Sum and display the sum
    sum_tree_ages = sum(tree_ages)
    print(f'{'Sum of all ages:':<34}{sum_tree_ages}')

    # Oldest and youngest age
    print(f'{'Oldest Age:':<34}{max(tree_ages)}')
    print(f'{'Youngest Age:':<34}{min(tree_ages)}')

    # Average Age
    average_age = sum_tree_ages / len(tree_ages)
    print(f'{'Average Age':<34}{average_age:.2f}')

    # Age groups
    count_seedling = tree_ages.count(0) + tree_ages.count(1) + tree_ages.count(2)
    print(f'{'Number of seedlings:':<34}{count_seedling}')

    sapling_aged_trees = [age for age in tree_ages if age >= 3 and age <= 20]
    print(f'{'Number of sapling-aged trees:':<34}{len(sapling_aged_trees)}')

    pole_staged_aged_trees = [age for age in tree_ages if age >= 21 and age <= 50]
    print(f'{'Number of pole staged-aged trees:':<34}{len(pole_staged_aged_trees)}')
    
    mature_aged_trees = [age for age in tree_ages if age >= 51 and age <= 100]
    print(f'{'Number of mature-aged trees:':<34}{len(mature_aged_trees)}')    

    old_growth_aged_trees = [age for age in tree_ages if age >= 101]
    print(f'{'Number of old growth-aged trees:':<34}{len(old_growth_aged_trees)}')


# Descending Function
def sort_descending(list_sorted):
    list_sorted.sort(reverse=True)
    return list_sorted


if __name__ == '__main__':
    main()