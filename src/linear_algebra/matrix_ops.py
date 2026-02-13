"""
Linear Algebra Utilities - Matrix Operations

This module provides basic matrix operations for data science applications.
"""

import numpy as np
from typing import Union, Tuple


def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Multiply two matrices.
    
    Args:
        A: First matrix (m x n)
        B: Second matrix (n x p)
        
    Returns:
        Product matrix (m x p)
        
    Example:
        >>> A = np.array([[1, 2], [3, 4]])
        >>> B = np.array([[5, 6], [7, 8]])
        >>> matrix_multiply(A, B)
        array([[19, 22],
               [43, 50]])
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError(f"Incompatible dimensions: {A.shape} and {B.shape}")
    
    return np.dot(A, B)


def matrix_transpose(A: np.ndarray) -> np.ndarray:
    """
    Transpose a matrix.
    
    Args:
        A: Input matrix
        
    Returns:
        Transposed matrix
        
    Example:
        >>> A = np.array([[1, 2, 3], [4, 5, 6]])
        >>> matrix_transpose(A)
        array([[1, 4],
               [2, 5],
               [3, 6]])
    """
    return A.T


def matrix_inverse(A: np.ndarray) -> np.ndarray:
    """
    Compute the inverse of a square matrix.
    
    Args:
        A: Square matrix
        
    Returns:
        Inverse of A
        
    Raises:
        ValueError: If matrix is not square or singular
        
    Example:
        >>> A = np.array([[1, 2], [3, 4]])
        >>> A_inv = matrix_inverse(A)
        >>> np.allclose(matrix_multiply(A, A_inv), np.eye(2))
        True
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")
    
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is singular and cannot be inverted")


def compute_eigenvalues(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute eigenvalues and eigenvectors of a matrix.
    
    Args:
        A: Square matrix
        
    Returns:
        Tuple of (eigenvalues, eigenvectors)
        
    Example:
        >>> A = np.array([[4, 2], [1, 3]])
        >>> eigenvalues, eigenvectors = compute_eigenvalues(A)
        >>> len(eigenvalues)
        2
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors


def frobenius_norm(A: np.ndarray) -> float:
    """
    Compute the Frobenius norm of a matrix.
    
    Args:
        A: Input matrix
        
    Returns:
        Frobenius norm (scalar)
        
    Example:
        >>> A = np.array([[1, 2], [3, 4]])
        >>> frobenius_norm(A)
        5.477225575051661
    """
    return np.linalg.norm(A, 'fro')


if __name__ == "__main__":
    # Example usage
    print("Matrix Operations Example")
    print("-" * 40)
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
    print("\nA * B:")
    print(matrix_multiply(A, B))
    
    print("\nTranspose of A:")
    print(matrix_transpose(A))
    
    print("\nInverse of A:")
    print(matrix_inverse(A))
    
    print("\nEigenvalues and Eigenvectors of A:")
    eigenvalues, eigenvectors = compute_eigenvalues(A)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
    
    print("\nFrobenius norm of A:")
    print(frobenius_norm(A))
