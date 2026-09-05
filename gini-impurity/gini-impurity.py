import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    # Write code here
    L = np.asarray(y_left, dtype = np.float64)
    R = np.asarray(y_right, dtype = np.float64)
    Lval, Lcnt = np.unique (L, return_counts = True)
    Rval, Rcnt = np.unique (R, return_counts = True)
    Lz = len(y_left)
    Rz = len(y_right)
    Lp, Rp = 0.0, 0.0
    if Lz == 0: 
        LGs = 0
    else:
        Lp = Lcnt/Lz
    if Rz == 0:
        RGs = 0
    else:
        Rp = Rcnt/Rz
    LGs = 1 - np.sum(Lp ** 2)
    RGs = 1 - np.sum(Rp ** 2)
    if Lz + Rz == 0:
        return 0.0
    else:
        return Lz/(Lz+Rz)*LGs + Rz/(Lz+Rz)*RGs
    pass