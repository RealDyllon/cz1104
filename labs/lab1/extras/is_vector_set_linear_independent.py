# Code to determine if a set of vectors is linearly independent

# '''Function to check if the generated vectors fulfil the independency requirements'''

# input two lists a & b, each contains 4 vectors
# Return "True" if any 3 pairs of vectors from (a1,b1),(a2,b2),(a3,b3),(a4,b4) are linearly independent

import numpy as np


def check_dependency(a, b):
    #
    for v1 in range(1, 3):  # 1st vector from 1 to 2
        for v2 in range(v1+1, 4):
            for v3 in range(v2+1, 5):
                squareMatrix = np.vstack(
                    (a[v1], b[v1], a[v2], b[v2], a[v3], b[v3]))
                determinant = np.linalg.det(squareMatrix)
                if determinant == 0:  # if determinant is 0, the vectors are not linearly dependent
                    return False

    # check if a0,b0 and any two random selected pairs of vectors are linearly independent
    for v1 in range(1, 4):  # 1st vector from 1 to 3
        for v2 in range(v1+1, 5):
            squareMatrix = np.vstack((a[0], b[0], a[v1], b[v1], a[v2], b[v2]))
            determinant = np.linalg.det(squareMatrix)
            if determinant == 0:  # if determinant is 0, the vectors are not linearly dependent
                return False
    return True
