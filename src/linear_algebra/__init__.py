"""
Linear Algebra package for data science.

This package provides essential linear algebra operations and algorithms.
"""

from .matrix_ops import (
    matrix_multiply,
    matrix_transpose,
    matrix_inverse,
    compute_eigenvalues,
    frobenius_norm
)

__all__ = [
    'matrix_multiply',
    'matrix_transpose',
    'matrix_inverse',
    'compute_eigenvalues',
    'frobenius_norm'
]
