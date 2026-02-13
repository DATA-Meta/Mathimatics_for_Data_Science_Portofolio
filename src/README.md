# Source Code

This directory contains Python modules and utility functions for the mathematics portfolio.

## Structure

```
src/
├── linear_algebra/      # Linear algebra utilities
├── calculus/           # Calculus and optimization functions
├── probability/        # Probability and statistics functions
├── optimization/       # Optimization algorithms
├── information/        # Information theory implementations
└── utils/             # General utility functions
```

## Modules

### linear_algebra/
- `matrix_ops.py` - Matrix operations and decompositions
- `vector_ops.py` - Vector operations
- `decompositions.py` - SVD, QR, LU decompositions
- `dim_reduction.py` - PCA and dimensionality reduction

### calculus/
- `derivatives.py` - Numerical derivatives and gradients
- `autodiff.py` - Automatic differentiation
- `integration.py` - Numerical integration methods

### probability/
- `distributions.py` - Probability distribution classes
- `stats.py` - Statistical functions
- `hypothesis.py` - Hypothesis testing functions
- `bayesian.py` - Bayesian inference utilities

### optimization/
- `optimizers.py` - Various optimization algorithms
- `gradient_descent.py` - Gradient descent variants
- `constrained.py` - Constrained optimization

### information/
- `entropy.py` - Entropy calculations
- `divergence.py` - KL divergence and related measures
- `mutual_info.py` - Mutual information

### utils/
- `visualization.py` - Plotting utilities
- `data_loader.py` - Data loading helpers
- `metrics.py` - Evaluation metrics

## Usage

```python
# Example: Using linear algebra module
from src.linear_algebra.matrix_ops import matrix_multiply, matrix_inverse
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = matrix_multiply(A, B)
A_inv = matrix_inverse(A)
```

## Development

### Adding New Modules

1. Create a new Python file in the appropriate subdirectory
2. Follow PEP 8 style guidelines
3. Include docstrings for all functions
4. Add unit tests in the corresponding test directory
5. Update this README

### Code Style

- Use type hints where appropriate
- Write clear docstrings (Google or NumPy style)
- Keep functions focused and modular
- Add examples in docstrings

## Testing

Run tests using pytest:
```bash
pytest tests/
```
