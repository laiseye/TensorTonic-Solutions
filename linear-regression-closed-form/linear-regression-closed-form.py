import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    x = np.asarray(X, dtype = np.float64)
    y = np.asarray(y, dtype = np.float64)
    w = np.linalg.inv(x.T @ x) @ x.T @ y
    return w.tolist()
    pass