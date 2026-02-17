# Alex Ha
# 2543681
# COP1000

# collaborator: none

"""
Psuedocode

Get blood sugar level as input as an integer (3 times)

Declare every level as included in the average
Compare the sugar levels
If 1st level is greater than 2nd then
    if 1st level greater than 3rd then
        disclude 1st level in average
    else 
        disclude 3rd level in average
else
    if 2nd level is greater than 3rd level
        disclude 2nd level in average 
    else 
        disclude 3rd level in average

Choose which average to use based on which level was discluded (3 if statements)
display the average calculated directly in the statement (using walrus operator: :=)

"""

# Input of blood sugar
first_blood_level = int(input("Enter first fasting blood sugar reading in mg/dL:  "))
second_blood_level = int(input("Enter second fasting blood sugar reading in mg/dL:  "))
third_blood_level = int(input("Enter third fasting blood sugar reading in mg/dL:  "))

# Disclude the highest 
first_level_included = True
second_level_included = True
third_level_included = True

if first_blood_level > second_blood_level:
    if first_blood_level > third_blood_level:
        first_level_included = False
    else: 
        third_level_included = False
else:
    if second_blood_level > third_blood_level:
        second_level_included = False
    else:
        third_level_included = False

# Calculate and display
NUMBER_OF_LEVELS_AVERAGED = 2
if not first_level_included:
    print(f"The average blood sugar for the patient is {(average := (second_blood_level + third_blood_level) / NUMBER_OF_LEVELS_AVERAGED):.1f} mg/dL")
if not second_level_included:
    print(f"The average blood sugar for the patient is {(average := (first_blood_level + third_blood_level) / NUMBER_OF_LEVELS_AVERAGED):.1f} mg/dL")
if not third_level_included:
    print(f"The average blood sugar for the patient is {(average := (second_blood_level + first_blood_level) / NUMBER_OF_LEVELS_AVERAGED):.1f} mg/dL")



