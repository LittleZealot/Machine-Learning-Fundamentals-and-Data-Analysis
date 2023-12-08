import math

# Problem 1: How many times does it have to fold to cross Mt. Fuji?
# Initial values
THICKNESS = 0.00008  # [m] meters
height_of_Fuji = 3776  # [m] meters
folds = 0
thickness = THICKNESS

# Folding loop
while thickness <= height_of_Fuji:
    folds += 1
    thickness *= 2

# Output the result
print("Problem 1: To reach the height of Mt. Fuji, {} folds are needed.".format(folds))

# Problem 2: Function corresponding to arbitrary thickness
proxima_centauri = 4.0175e+16

# Function to calculate folds needed
def nfolds(thickness, height):
    folds = 0
    while thickness <= height:
        folds += 1
        thickness *= 2
    return folds

# Calculate folds to Proxima Centauri
folds_to_centauri = nfolds(THICKNESS, proxima_centauri)
print("Problem 2: Folds needed to reach Proxima Centauri: ", folds_to_centauri)

# Problem 3: Required length of paper
# Function to calculate the length of paper needed
def len_paper(thickness, number):
    n = math.pow(2, number)
    return math.pi * thickness / 6 * (n + 4) * (n - 1)

# Function to calculate the length of paper to a specific height
def len_paper2(thickness, height):
    folds = nfolds(thickness=thickness, height=height)
    n = math.pow(2, folds)
    return math.pi * thickness / 6 * (n + 4) * (n - 1)

# Output the lengths of paper needed
print("Problem 3: Length of paper needed to reach the Moon: ", len_paper(THICKNESS, 43))
print("Problem 3: Length of paper needed to reach Mt. Fuji: ", len_paper(THICKNESS, folds))
print("Problem 3: Length of paper needed to reach Proxima Centauri: ", len_paper2(THICKNESS, proxima_centauri))
