import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array.
    """
    # Write code here

    labels = np.asarray (y_train, dtype = int)
    samples = np.asarray (X_test, dtype = int)
    sz = samples.shape[0]
    val, idx, cnt = np.unique (labels, return_index = True, return_counts = True)
    new_arr = np.flatnonzero (cnt == cnt.max()) 
    tmp = np.argmin(idx[new_arr])
    ans = val[new_arr[tmp]]
    return np.full (sz, ans, dtype = int)