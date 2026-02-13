"""
Example Jupyter Notebook: Introduction to Linear Algebra

This notebook demonstrates basic linear algebra operations for data science.
"""

# Note: To use this as a template, save it with .ipynb extension
# You can create actual Jupyter notebooks using the Jupyter interface

NOTEBOOK_TEMPLATE = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Introduction to Linear Algebra for Data Science\n",
                "\n",
                "This notebook covers fundamental linear algebra concepts:\n",
                "1. Vectors and Matrices\n",
                "2. Matrix Operations\n",
                "3. Eigenvalues and Eigenvectors\n",
                "4. Applications in Data Science"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Import libraries\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import sys\n",
                "sys.path.append('../src')\n",
                "\n",
                "from linear_algebra.matrix_ops import matrix_multiply, compute_eigenvalues"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Vectors and Matrices\n",
                "\n",
                "Vectors and matrices are fundamental data structures in data science."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Create vectors\n",
                "v1 = np.array([1, 2, 3])\n",
                "v2 = np.array([4, 5, 6])\n",
                "\n",
                "print('Vector 1:', v1)\n",
                "print('Vector 2:', v2)\n",
                "print('Dot product:', np.dot(v1, v2))"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Create matrices\n",
                "A = np.array([[1, 2], [3, 4]])\n",
                "B = np.array([[5, 6], [7, 8]])\n",
                "\n",
                "print('Matrix A:')\n",
                "print(A)\n",
                "print('\\nMatrix B:')\n",
                "print(B)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Matrix Operations\n",
                "\n",
                "Key matrix operations used in data science."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Matrix multiplication\n",
                "C = matrix_multiply(A, B)\n",
                "print('A × B =')\n",
                "print(C)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Eigenvalues and Eigenvectors\n",
                "\n",
                "Important for PCA and understanding transformations."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Compute eigenvalues and eigenvectors\n",
                "eigenvalues, eigenvectors = compute_eigenvalues(A)\n",
                "print('Eigenvalues:', eigenvalues)\n",
                "print('Eigenvectors:')\n",
                "print(eigenvectors)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Application: Principal Component Analysis (PCA)\n",
                "\n",
                "PCA is based on eigenvalue decomposition."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Generate sample data\n",
                "np.random.seed(42)\n",
                "data = np.random.randn(100, 2) @ np.array([[2, 0.5], [0.5, 1]])\n",
                "\n",
                "# Compute covariance matrix\n",
                "cov_matrix = np.cov(data.T)\n",
                "print('Covariance matrix:')\n",
                "print(cov_matrix)\n",
                "\n",
                "# Compute eigenvectors (principal components)\n",
                "eigenvalues, eigenvectors = compute_eigenvalues(cov_matrix)\n",
                "print('\\nPrincipal components (eigenvectors):')\n",
                "print(eigenvectors)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Visualize data and principal components\n",
                "plt.figure(figsize=(10, 6))\n",
                "plt.scatter(data[:, 0], data[:, 1], alpha=0.5)\n",
                "plt.arrow(0, 0, eigenvectors[0, 0]*eigenvalues[0], eigenvectors[1, 0]*eigenvalues[0],\n",
                "          head_width=0.3, head_length=0.3, fc='red', ec='red', label='PC1')\n",
                "plt.arrow(0, 0, eigenvectors[0, 1]*eigenvalues[1], eigenvectors[1, 1]*eigenvalues[1],\n",
                "          head_width=0.3, head_length=0.3, fc='blue', ec='blue', label='PC2')\n",
                "plt.xlabel('Feature 1')\n",
                "plt.ylabel('Feature 2')\n",
                "plt.title('PCA: Data with Principal Components')\n",
                "plt.legend()\n",
                "plt.grid(True)\n",
                "plt.axis('equal')\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Summary\n",
                "\n",
                "In this notebook, we covered:\n",
                "- Basic vector and matrix operations\n",
                "- Eigenvalues and eigenvectors\n",
                "- Application to PCA for dimensionality reduction\n",
                "\n",
                "## Exercises\n",
                "\n",
                "1. Create your own matrices and compute their products\n",
                "2. Verify that eigenvectors are indeed eigenvectors (Av = λv)\n",
                "3. Apply PCA to a higher-dimensional dataset\n",
                "4. Explore SVD as an alternative to eigenvalue decomposition"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# To create this as an actual notebook, you can run:
# jupyter nbconvert --to notebook --execute notebook_template.py
