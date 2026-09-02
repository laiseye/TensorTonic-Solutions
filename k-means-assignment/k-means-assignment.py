import numpy as np

def k_means_assignment(points: list, centroids: list) -> np.ndarray:
    P = np.asarray(points, dtype=np.float64)
    C = np.asarray(centroids, dtype=np.float64)
    
    if P.ndim == 1:
        P = P.reshape(-1, 1)
    if C.ndim == 1:
        C = C.reshape(-1, 1)
        
    distances = np.sum((P[:, None, :] - C[None, :, :]) ** 2, axis=-1)
    return np.argmin(distances, axis=-1).tolist()