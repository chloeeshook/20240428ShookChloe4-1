"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00  
numChars = 18  
color = "black" 
woodType = "oak" 

# Base charge for any sign
charge += 35.00

# Charge for additional characters (beyond the first 5)
if numChars > 5:
    charge += (numChars - 5) * 4

# Charge for oak wood
if woodType == "oak":
    charge += 20.00

# Charge for gold-leaf lettering
if color == "gold":
    charge += 15

# Output Charge for this sign
print("The charge for this sign is $" + str(charge))
