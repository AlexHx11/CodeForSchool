# Alex Ha
# 2543681
# COP1000

# Collaborator: none

"""
Psuedocode

Define a function that takes the eyelet pairs and amount of shoestring pairs as parameters
    Define price per eyelet pair as 0.50 (50 cents)
    Multiply (*) the price per eyelet pair by the amount of eyelet pairs and save it as price per shoe string pair
    Multiply (*) the price per shoe string pair by the amount of shoestring pairs total and save it as the subtotal
    Return the subtotal

"""

def get_subtotal(eyelet_pairs, num_shoestring_pairs) :
    # 50 cent constant
    PRICE_PER_EYELET_PAIR = 0.50

    # Math for subtotal
    price_per_shoestring = eyelet_pairs * PRICE_PER_EYELET_PAIR
    subtotal = num_shoestring_pairs * price_per_shoestring

    return subtotal