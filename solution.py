import pandas as pd
import numpy as np


def pseudoinverse(M):
    """
        Get the pseudoinverse of M
    """
    return np.linalg.inv(M.T @ M) @ M.T


def ordinary_least_squares(M, c):
    """
        Get the ordinary least squares solution of Mx = c
        This is the pseudoinverse of M mult by c
    """
    return pseudoinverse(M) @ c


def get_squared_error(M, x, c):
    """
        Get the OLS error of Mx = c: ||Mx - c||^2 - i.e. the residuals of your OLS regression
        These are then normalised by the problem length scale, namely ||c||^2           
    """
    residual = M@x - c
    return (residual.T @ residual) / (c.T @ c)



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

    # Get the error of the current x
    target_x_error = get_squared_error(A, target_x, b)
    print('Provided x squared error = ', target_x_error)

    # Get the error of the OLS solution
    ols_x = ordinary_least_squares(A, b)
    ols_x_error = get_squared_error(A, ols_x, b)
    print('OLS x squared error = ', ols_x_error)

    # Output the ols_x we want
    with open('./x_ols.txt', 'w') as f:
        for x_i in ols_x:
            f.write(str(x_i))
            f.write('\n')
