import numpy as np

def k_means_assignment(points: list, centroids: list) -> np.ndarray:
    p = np.asarray(points, dtype = int)
    c = np.asarray(centroids, dtype = int) 
    if p.ndim == 1:
        p = p.reshape(-1, 1)
    if c.ndim == 1:
        p = p.reshape(-1, 1)
    dist = np.sum((p[:, None, :] - c[None, :, :])**2, axis = -1)
    return np.argmin(dist, axis = -1).tolist()