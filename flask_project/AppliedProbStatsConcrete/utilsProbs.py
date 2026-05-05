import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

#  https://cs229.stanford.edu/lectures-spring2022/main_notes.pdf  pg.15
#  θ = (((X^T)*X)^-1)*(X^T)*(~>y)



# this is fro creating a matrix, but of the entire dataFrame
# So, this doesn't have the 1 column, and Y target column is still included
def MatrixCreator(df):    
    matrix = df.to_numpy()
    return matrix



def MatrixDummyColumn(df):
    # local matrix is the whole CSV file as a dataFrame
    localMatrix = MatrixCreator(df)
    
    
    # finds the index for the last column (target) so it can be removed
    targetIndex = localMatrix.shape[1] - 1
    
    # remove the last column
    localMatrixCleaned = np.delete(localMatrix, targetIndex, axis=1)
    
    finalMatrix = np.insert(localMatrixCleaned, 0, 1, axis=1)
    
    return finalMatrix



def MatrixMultiplier(matrix1, matrix2):
    result = np.matmul(matrix1, matrix2)
    return result
    
    
    
def MatrixTranspose(matrix):    
    #matrix = MatrixCreator(df)
    transposedMatrix = np.transpose(matrix)
    return transposedMatrix


# for non-square matrix:
#     numpy.linalg.pinv (Moore-Penrose Pseudoinverse) --> np.linalg.pinv(A)
#     numpy.linalg.lstsq (Least-Squares Solution)     --> np.linalg.lstsq(A, b)
def MatrixInverse(matrix):
    inversedMatrix = np.linalg.pinv(matrix)
    return inversedMatrix



#   this if for y (target vector)
def TargetVector(df):
    y = df.iloc[:, -1].to_numpy().reshape(-1, 1)
    return y
    


#  θ = (((X^T)*X)^-1)*(X^T)*(~>y)
def ThetaFinder(df):
    X = MatrixDummyColumn(df)
    X_T = MatrixTranspose(X)
    y = TargetVector(df)
    
    X_T_mult_X =  MatrixMultiplier(X_T, X)
    X_T_mult_y = MatrixMultiplier(X_T, y)
    
    X_T_mult_X_inverse = MatrixInverse(X_T_mult_X)
    
    theta = MatrixMultiplier(X_T_mult_X_inverse, X_T_mult_y)
    
    print("THETA MATRIX:")
    print(theta)
        
        
    # for finding epsilons matrix
    y_hat = MatrixMultiplier(X, theta)
    epsilon = y - y_hat
    
    print("Epsilon (residuals):")
    print(epsilon)
    
    return theta, epsilon, y_hat
    
    
    
    
def Predict(X_new, theta):
    
    # add column of 1s for intercept
    X_new = np.insert(X_new, 0, 1, axis=1)
    
    y_pred = np.matmul(X_new, theta)
    return y_pred




    
