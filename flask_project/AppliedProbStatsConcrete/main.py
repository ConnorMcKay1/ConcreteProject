import numpy as np
import pandas as pd

from .utilsStats import *
from .plotting import *
from .utilsProbs import *


# UPDATED VERSION FOR FLASK COMPATABILITY


def load_dataset(csv_file):
    """
    Loads dataset safely.
    No assumptions about path.
    """
    return pd.read_csv(csv_file)



def predict_concrete(csv_file, x_new):
    df = pd.read_csv(csv_file)

    theta, epsilon, y_hat = ThetaFinder(df)

    y_pred = Predict(np.array([x_new]), theta)

    return {
        "theta": theta,
        "epsilon": epsilon,
        "y_hat": y_hat,
        "y_pred": y_pred,
        "df_shape": df.shape
    }


# making sure everything is returned for use in the front end
def run_diagnostics(csv_file):
    """
    Returns everything needed for plotting.
    """
    df = load_dataset(csv_file)

    theta, epsilon, y_hat = ThetaFinder(df)
    y_actual = TargetVector(df)

    return {
        "theta": theta,
        "epsilon": epsilon,
        "y_hat": y_hat,
        "y_actual": y_actual
    }


#   used for local testing
if __name__ == "__main__":
    test_file = "data_1.csv"

    test_vector = [550, 0, 0, 165, 3.3, 584, 607, 7]

    theta, y_pred, df = predict_concrete(test_file, test_vector)

    print("PREDICTION:", y_pred)
    print("THETA:", theta)