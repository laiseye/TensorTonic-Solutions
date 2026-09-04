import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    y = np.asarray(y, dtype = np.float64)
    sz = y.shape[0]
    if sz == 0:
        return 0.0
    val, cnt = np.unique (y, return_counts = True)
    p = cnt[cnt > 0] / sz
    H = -np.sum(p*np.log2(p))
    return H
    pass