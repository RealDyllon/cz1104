# Code for random binary number generation

# Python program for random
# binary string generation

import random

# Function to create random binary string of length p


def rand_key(p):

    # Variable to store in an array
    key = []

    # Loop to find the string
    # of desired length
    for i in range(p):

        # randint function to generate
        # 0, 1 randomly and add
        # the result into arry
        key.append(random.randint(0, 1))
    return(key)
