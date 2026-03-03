import numpy as np

def varimax(loadings, max_iter=1000, tol=1e-8):
    """
    Applique la rotation Varimax aux loadings d'une PCA.
    Entrée : loadings (array-like) de forme (n_wavelengths, n_components)
    """
    X = np.asarray(loadings)
    n_rows, n_cols = X.shape
    print(f"Varimax: n_rows={n_rows}, n_cols={n_cols}")
    if n_cols < 2:
        return X

    # 1. Normalisation de Kaiser
    row_norms = np.sqrt(np.sum(X**2, axis=1, keepdims=True))
    # X_normalized = X / row_norms
    X_normalized = X

    # Initialisation de la matrice de rotation
    R = np.eye(n_cols)

    for i in range(max_iter):
        # Calcul des loadings rotés actuels
        X_rot = np.dot(X_normalized, R)
        
        # Algorithme de rotation de Kaiser
        # On calcule le gradient vers lequel on veut "pousser" les loadings
        # Cela revient à maximiser la variance des carrés
        d = np.dot(X_normalized.T, X_rot**3 - (1.0/n_rows) * np.dot(X_rot, np.diag(np.sum(X_rot**2, axis=0))))
        
        # SVD pour trouver la rotation orthogonale la plus proche (Procrustes)
        U, S, Vt = np.linalg.svd(d)
        R_new = np.dot(U, Vt)
        
        # Vérification de la convergence
        if np.abs(np.abs(np.linalg.det(np.dot(R.T, R_new))) - 1) < tol:
            break
            
        R = R_new

    # 2. Dénormalisation et application de la rotation finale
    X_final = np.dot(X_normalized, R) * row_norms
    
    return X_final, R