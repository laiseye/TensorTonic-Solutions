import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here
    x = np.asarray(X, dtype = np.float64)
    y = np.asarray(y, dtype = np.float64)
    I = np.eye(x.shape[1])
    w = np.linalg.inv(x.T @ X + lam * I) @ x.T @ y
    return w.tolist()
    pass