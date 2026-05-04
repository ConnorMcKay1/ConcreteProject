import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


'''
mean, variance  ->~done
correlation     ->~done
regression slope
covariance
'''

def Mean(data):
    mean = (np.mean(data))
    return mean
    
def StandardDeviation(data):
    standard_deviation = (np.std(data))
    return standard_deviation
    
def Correlation(X, Y):
    matrix = np.corrcoef(X, Y)
    correlation = matrix[0, 1] 
    return correlation
    

def RegressionLine(X, Y):
    result = stats.linregress(X, Y)
    return result
    

def Covariance(X, Y):
    matrix = np.cov(X, Y, rowvar = False)
    covariance = matrix[0, 1] 
    return covariance


    # get the distribution of a SINGLE column
def Distribution(data):
    mu, sigma = stats.norm.fit(data)
    return mu, sigma









