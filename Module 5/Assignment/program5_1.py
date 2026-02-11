# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode

Import the subtotal function

Define the grand total as 0

Prompt the user for the amount of types of shoestrings they will buy
Loop through for the amount of different types of shoe strings
    For each loop, prompt the user for the number of eyelet pair and and amount of shoestring pairs of that type
    Pass these arguments to a function that calculates the subtotal
    Display the subtotal
    Add the subtotal to the grand total

Display the grand total

Check that this program is the main one by checking if the name of the execution is main

"""

import shoestring_subtotal

def main():
    # Input
    num_shoestring_types = int(input("Enter the number of different types of shoelaces being purchased: "))

    # Define Grand Total
    grand_total = 0

    # Loops for Prompts
    for num_type in range(num_shoestring_types):
        print(f'Item {num_type + 1}: ')

        eyelet_pairs = int(input("Enter the number of eyelet pairs: "))
        amt_shoestring_pairs = int(input("Enter the quantity: "))
        subtotal = shoestring_subtotal.get_subtotal(eyelet_pairs, amt_shoestring_pairs)

        print(f'Subtotal for Item {num_type + 1}: ${subtotal:,.2f} \n')
        grand_total += subtotal

    # Final grand total
    print(f"Total: ${grand_total:,.2f}")

if __name__ == '__main__' :
    main()
