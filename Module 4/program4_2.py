# Alex Ha
# 2543681
# COP1000

# collaborator: none

"""
Pseudocode

While the FSA contribution isn't within range (above 3200)
    Prompt the user for their FSA contribution and save it

Define count of FSA expenditures as 0
Define total FSA expenditures as 0
While the FSA expenditure amount isn't 0
    Prompt the user for their FSA expenditure amount
    Increment (+=) the count of expenditures by 1
    Increment (+=) the total FSA expenditures by the expenditure amount

If total FSA expenditures is equal to the contributions
    Display that the expenditures and contributions are equal
If total FSA expenditures is greater than contributions
    Display that the expenditures exceed the contributions by a certain amount (expenditures - contributions)
If total FSA expenditures is less than contributions
    Display that the expenditures fall short of the contributions by a certain amount (contributions - expenditures)
"""

# Program

# Prompt and save the FSA contribution
MAX_CONTRIBUTION = 3200
while (contribution := int(input(f"Enter your FSA contribution for the year as a whole number (max allowed is {MAX_CONTRIBUTION}): "))) > MAX_CONTRIBUTION :
    print(f"The max contribution is ${MAX_CONTRIBUTION}")

# Loop and collect amount and value of expenditures
expenditures = 0
count_of_expenditures = 0
while (expenditure_amount := int(input("Enter the FSA expenditure as a whole number (enter 0 to finish): "))) != 0:
    expenditures += expenditure_amount
    count_of_expenditures += 1

# Display count, total
print(f"You have a count of {count_of_expenditures} FSA expenditures for the year.")
print(f"You have accumulated a total of ${expenditures} for the year.")

# Display analysis
if expenditures == contribution:
    print("Your expenditure total is the same as your FSA contribution.")
elif expenditures > contribution:
    print(f"Your expenditure total is ${expenditures - contribution} over your FSA contribution for the year.")
elif contribution > expenditures:
    print(f"Your expenditure total is ${contribution - expenditures } under your FSA contribution for the year.")
