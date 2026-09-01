import numpy as np

def knn_distance(X_train: list, X_test: list, k: int) -> np.ndarray:
    """
    Returns a NumPy array with shape (n_test, k).
    """
    # Write code here
    train = np.asarray(X_train, np.float64)
    test = np.asarray(X_test, np.float64)
    if train.ndim == 1:
        train = train.reshape(-1, 1)
    if test.ndim == 1:
        test = test.reshape(-1, 1)
    dist = np.sum((test[:, None, :] - train[None, :, :])**2, axis = -1)
    dist = np.argsort(dist, axis = -1)
    ans = dist[:, :k]
    if k > train.shape[0]:
        adding = np.full((test.shape[0], k - train.shape[0]), -1)
        ans = np.concatenate((ans, adding), axis = -1)
    ans = ans.astype(int)
    return ans
    pass