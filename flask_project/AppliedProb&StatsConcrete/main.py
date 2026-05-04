import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.io import arff


'''

SIMPLE RELATIONSHIPS:
    Which variables are related to the output?
    Are relationships linear or monotonic?
        
PREDICTIVE MODELING:
    How well can I predict the output from the inputs?
    ****Which variables matter most?****  use this to find out which variable affects strenght the most?

EFFECTS OF INTERACTION:
    Do variables combine in not obvious ways?


  ***************************
** OvEr ArChInG ReSeArCh AiM **

PREDICT CONCRETE STRENGHT based on the ingredient input amounts/auntities?
    --> Wounldn't this just yield the "ideal"
    *   concrete mix? (ignoring prediction errors obviously)    *
    **************************************************************

'''
        #   SciPy Documentation Recomended
    # Make All 8 Variables in Scatter Plots
    # Look into Correlation Coefficient (r)
    #   (Measures the Strgth & dir. of linear relationship)
    # Regression Analysis: would create a "line of best fit"
    #                      to model the relationship & make predictions                      
##################################################################

from utilsStats import *
from plotting import *
from utilsProbs import *

print("test test turnip \n")

#----------------------------------------------------------------------------------------------------------------------------------
current_dir = os.path.dirname(__file__)  # folder where main.py lives

    # This is 'concrete_compresssive_strencth.csv --> (data_1)
dataFile = os.path.join(current_dir, "data_1.csv")

    # This is Dataset2 - Data.csv --> (data_3)
#dataFile = os.path.join(current_dir, "data_3.csv")

    # This is from OpenML --> data_4
#dataFile = os.path.join(current_dir, "data_4.csv")


#----------------------------------------------------------------------------------------------------------------------------------
    # This is 'concrete_compresssive_strencth.csv --> (data_1)
#dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/data_1.csv"
 
    # This is 'concrete_resistance.csv  --> (data_2) --> this is the one with 10 columns and 2 differenct variables
#dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/data_2.csv"

    # This is Dataset2 - Data.csv --> (data_3)
#dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/data_3.csv"

    # This is from OpenML --> data_4
#dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/data_4.csv"

#----------------------------------------------------------------------------------------------------------------------------------



    # just reading in the 1 of the data sets to get the 2 columns for the scatter
    # for the scatter plot method below
def DataReadIn(csvFile):
    df = pd.read_csv(csvFile)
    
    xAxis_Column = df.iloc[:, 0].tolist()
    yAxis_Column = df.iloc[:, 8].tolist()
    return xAxis_Column, yAxis_Column, df

xAxis_Column, yAxis_Column, df = DataReadIn(dataFile)


    # just a bunch of calls to the functions in utilsStats.py
def UtilsPrinter():
    print(xAxis_Column)
    print("----------------------------------------------------------------------------------------")
    print(yAxis_Column)
    print("------------------")
    Mean(xAxis_Column)
    print("------------------")
    StandardDeviation(xAxis_Column)
    print("------------------")
    Correlation(xAxis_Column, yAxis_Column)
    print("------------------")
    RegressionLine(xAxis_Column, yAxis_Column)
    print("------------------")
    Covariance(xAxis_Column, yAxis_Column)


def test():
    print("Conversion complete!")


# example from first line for data_1.csv
# 550, 0, 0, 165, 3.3, 584, 607, 7, 49.71
if __name__ == "__main__":
    print("main runner")
    
    theta, epsilon, y_hat = ThetaFinder(df)
    
    x_new = np.array([[550, 0, 0, 165, 3.3, 584, 607, 7]])
    y_pred = Predict(x_new, theta)

    print("PREDICTION OF y:")
    print(y_pred)
    
    y = TargetVector(df)
    PlotDiagnostics(y, y_hat, epsilon)
    
    
    