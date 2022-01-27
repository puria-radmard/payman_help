from bdb import set_trace
import pandas as pd
import numpy as np
from solution import get_squared_error
import matplotlib.pyplot as plt


def regularised_ordinary_least_squares(M, c, x_target, l):
    """
        Get the regularised ordinary least squares solution of Mx = c
        Regularisation point is x_target, by default 0 to match the Bayesian regularisation case.
        The regularisation term weight is l (lambda is not allowed by python)
        The solution is given in README.md
    """
    m, n = A.shape
    matrix_term = np.linalg.inv((M.T @ M) + (l * np.eye(n)))
    vector_term = (l * x_target + M.T @ c)
    return matrix_term @ vector_term


def get_normalised_regularisation_error(x_solution, x_target):
    """
        Return the normalised normalised regularisation error (without weighting)
            = ||x_solution - x_target||^2 / (||x_target||^2)
    """
    numerator = (x_solution - x_target).T @ (x_solution - x_target)
    denominator = x_target.T @ x_target
    return numerator / denominator


if __name__ == '__main__':

    # Hardcoded all the file names
    A_FILE_NAME = './email_folder/A.xlsx'
    B_FILE_NAME = './email_folder/b.xlsx'
    TARGET_X_FILE_NAME = './email_folder/target X.xlsx'

    # Get the matrices out of the files
    A = pd.read_excel(A_FILE_NAME, header=None).values
    b = pd.read_excel(B_FILE_NAME, header=None).values
    target_x = pd.read_excel(TARGET_X_FILE_NAME, header=None).values

    # Reshape the matrices to make things easier
    m, n = A.shape
    b = b.reshape(m)
    target_x = target_x.reshape(n)

    # Prepare a series of 100 lambdas to try out
    # Remember: 
    #   as lambda -> 0, recover OLS case (solution.py) => minimal target error
    #   as lambda -> inf, recover ther target x => minimal regularisation error
    lambdas = np.logspace(-10, 5, 100)

    # Initialise our results we want to plot later
    target_errors = [] # These are errors in Ax = b, which should increase as lambda is increased
    regularisation_errors = []  # These are errors in x = x_target, which should decrease as lambda is increased

    # Iterating over regularsiation weights...
    # tqdm just creates a nice loading bar
    for _l in lambdas:

        # Get the regularised solution
        x_regularised = regularised_ordinary_least_squares(A, b, target_x, _l)

        # Find the errors and add them to our results
        target_errors.append(get_squared_error(A, x_regularised, b))
        regularisation_errors.append(get_normalised_regularisation_error(x_regularised, target_x))

    # Now, let's plot our results against the lambdas used to generate them
    plt.plot(lambdas, target_errors, label = 'Target error (Ax = b error)')
    plt.plot(lambdas, regularisation_errors, label = 'Regularisation error (x = target x error)')
    plt.xlabel('$\lambda$')
    plt.legend()
    plt.show()
