'''
create a linear regression method that will take the regressionLine of all the columns of each file:
  EXAMPLE -->     xAxis_Column = df.iloc[:, FOR N-1  in File].tolist() yAxis_Column = df.iloc[:, 8].tolist()
'''
'''
then do this for each of the graphs; so just 'For N .csv files in directory, run NewRegressionLine method'
'''



import pandas as pd
import io
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from .utilsStats import *


''' LEGACY '''
    ## This was for printing all of the REGRESSION LINES for all of the INGREDIENTS
    # creates the window with all the X ingrediantes against output Y (strength)
def LinearRegression_AllColumns(df):

    y_col_name = df.columns[-1]
    x_columns = df.columns[:-1]

    num_plots = len(x_columns)

    cols = 3
    rows = (num_plots + cols - 1) // cols

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(18, 6 * rows),
        constrained_layout=True
    )

    axes = axes.flatten()

    for i, col_name in enumerate(x_columns):
        x = df[col_name]
        y = df[y_col_name]

        result = RegressionLine(x, y)

        ax = axes[i]

        ax.scatter(x, y)

        slope = result.slope
        intercept = result.intercept
        ax.plot(x, slope * x + intercept, color='red')      # the regression line itself 

        ax.set_title(col_name)
        ax.set_xlabel(col_name)
        ax.set_ylabel(y_col_name)

    for j in range(num_plots, len(axes)):
        fig.delaxes(axes[j])

    #fig.savefig("my_plot.png")
    plt.show()




def DistributionPlot(df):
    print("plot the damn distributions!")

    num_plots = len(df.columns)

    cols = 3
    rows = (num_plots + cols - 1) // cols

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(18, 6 * rows),
        constrained_layout=True
    )

    axes = axes.flatten()

    for i, col_name in enumerate(df.columns):
        ax = axes[i]

        data = df[col_name].dropna()  # safer

        mu, sigma = stats.norm.fit(data)

        x = np.linspace(data.min(), data.max(), 100)

        ax.hist(data, bins=30, density=True, alpha=0.6, label='Data Histogram')
        ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', label='Fitted Normal PDF')

        ax.set_title(f'Column: {col_name}')
        ax.set_xlabel(col_name)
        ax.set_ylabel('Density')
        ax.legend()

    for j in range(num_plots, len(axes)):
        fig.delaxes(axes[j])

    #fig.savefig("my_plot.png")
    plt.show()
    
    
    
    
def PlotDiagnostics(y, y_hat, epsilon):
    y = y.flatten()
    y_hat = y_hat.flatten()
    epsilon = epsilon.flatten()
    error_mag = np.abs(epsilon)
    
    fig, axs = plt.subplots(1, 3, figsize=(18,5))
    
    # predicted vs actual
    axs[0].scatter(y, y_hat, alpha=0.7)
    min_val = min(y.min(), y_hat.min())
    max_val = max(y.max(), y_hat.max())
    axs[0].plot([min_val, max_val], [min_val, max_val], 'r--')
    axs[0].set_title("Predicted vs Actual")
    axs[0].set_xlabel("Actual")
    axs[0].set_ylabel("Predicted")
    axs[0].grid(True)
    
    # residuals vs prediction
    axs[1].scatter(y_hat, epsilon, alpha=0.7)
    axs[1].axhline(0, color='red', linestyle='--')
    axs[1].set_title("Residuals")
    axs[1].set_xlabel("Predicted")
    axs[1].set_ylabel("Error")
    axs[1].grid(True)
    
    # error magnitude plot
    sc = axs[2].scatter(y, y_hat, c=error_mag, cmap='viridis', alpha=0.8)
    axs[2].plot([min_val, max_val], [min_val, max_val], 'r--')
    axs[2].set_title("Error Magnitude")
    axs[2].set_xlabel("Actual")
    axs[2].set_ylabel("Predicted")
    axs[2].grid(True)
    
    fig.colorbar(sc, ax=axs[2], label="|Error|")
    
    plt.tight_layout()
    plt.show()