# Alex Ha
# 2543681
# COP1000

# collaborator: none

"""
Psuedocode:

Input the amount of ordered guitar picks as an integer

Define the cost per pick based on amount ordered
If ordered guitar picks at least 36 then charge 19 cents each
If ordered guitar picks at least 24 then charge 21 cents each
If ordered guitar picks at least 24 then charge 23 cents each
Otherwise charge 25 cents each

Multiply the price per pick by the amount of picks ordered to find the total cost
Display the total cost of picks.

"""

# Input for guitar picks
guitar_picks_ordered = int(input("How many guitar picks do you wish to buy? "))

# Define price per pick
price_per_pick = None # in dollars
if guitar_picks_ordered >= 36: 
    price_per_pick = 0.19
elif guitar_picks_ordered >= 24:
    price_per_pick = 0.21
elif guitar_picks_ordered >= 12:
    price_per_pick = 0.23
else: 
    price_per_pick = 0.25

# Calculate cost and display
cost_of_picks = guitar_picks_ordered * price_per_pick
print(f'Total cost of guitar picks is: ${cost_of_picks:,.2f}')