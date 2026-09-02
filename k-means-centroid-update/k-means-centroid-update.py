import numpy as np

def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    p = np.asarray(points, dtype = np.float64)
    a = np.asarray(assignments, dtype = int)
    if p.ndim == 1:
        p = p.reshape(-1, 1)
    a = a.ravel() # ép a chắc chắn phải thành mảng 1 chiều
    centroids = []
    for i in range (k):
        cum_i = p[a == i] 
        if len(cum_i) == 0:
            vector_0 = np.zeros(p.shape[1], dtype = np.float64)
            centroids.append(vector_0.tolist())
        else:
            centroids.append(np.mean(cum_i, axis = 0, dtype = np.float64).tolist())
    return centroids
    pass