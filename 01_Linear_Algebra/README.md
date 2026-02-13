# Linear Algebra for Data Science

This directory contains implementations and examples of linear algebra concepts essential for data science.

## Topics Covered

### 1. Vectors and Matrices
- Vector operations (addition, scalar multiplication, dot product)
- Matrix operations (addition, multiplication, transpose)
- Special matrices (identity, diagonal, symmetric)

### 2. Matrix Decompositions
- LU Decomposition
- QR Decomposition
- Cholesky Decomposition
- Singular Value Decomposition (SVD)

### 3. Eigenvalues and Eigenvectors
- Computing eigenvalues and eigenvectors
- Diagonalization
- Applications in stability analysis

### 4. Applications
- Principal Component Analysis (PCA)
- Dimensionality Reduction
- Recommender Systems
- Image Compression using SVD

## Files

- `vectors_matrices.py` - Basic vector and matrix operations
- `decompositions.py` - Matrix decomposition implementations
- `eigenvalues.py` - Eigenvalue and eigenvector computations
- `pca_example.ipynb` - PCA implementation and visualization
- `svd_image_compression.ipynb` - Image compression using SVD

## Getting Started

```python
import numpy as np
from vectors_matrices import vector_dot_product, matrix_multiply

# Example: Vector operations
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot_product = vector_dot_product(v1, v2)
print(f"Dot product: {dot_product}")
```

## Key Concepts

- **Why Linear Algebra?**: Forms the foundation for understanding data representations, transformations, and many ML algorithms
- **Real-world Applications**: Image processing, natural language processing, dimensionality reduction, graph analysis
