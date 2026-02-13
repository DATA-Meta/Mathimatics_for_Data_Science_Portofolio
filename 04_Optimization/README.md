# Optimization for Data Science

This directory contains implementations of optimization algorithms used in machine learning and data science.

## Topics Covered

### 1. Convex Optimization
- Convex functions and sets
- Convex optimization problems
- Global vs local optima
- KKT conditions

### 2. Gradient-Based Methods
- Gradient Descent (GD)
- Stochastic Gradient Descent (SGD)
- Mini-batch Gradient Descent
- Momentum methods
- Adam, RMSprop, AdaGrad

### 3. Advanced Optimization
- Newton's Method
- Quasi-Newton methods (BFGS)
- Conjugate Gradient
- Coordinate Descent

### 4. Constrained Optimization
- Lagrange multipliers
- KKT conditions
- Penalty methods
- Support Vector Machines (SVM) optimization

### 5. Applications
- Training neural networks
- Hyperparameter tuning
- Resource allocation
- Portfolio optimization

## Files

- `gradient_methods.py` - Various gradient descent implementations
- `newton_method.py` - Newton's method and variants
- `constrained_optimization.py` - Constrained optimization algorithms
- `optimizer_comparison.ipynb` - Comparing different optimizers
- `svm_optimization.ipynb` - SVM dual problem optimization

## Getting Started

```python
from gradient_methods import adam_optimizer
import numpy as np

# Example: Using Adam optimizer
def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def rosenbrock_grad(x):
    dx = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)
    dy = 200 * (x[1] - x[0]**2)
    return np.array([dx, dy])

initial = np.array([0.0, 0.0])
optimum = adam_optimizer(rosenbrock_grad, initial, learning_rate=0.001, iterations=1000)
print(f"Optimum found at: {optimum}")
```

## Key Concepts

- **Why Optimization?**: Core of training machine learning models efficiently
- **Gradient Descent**: Most fundamental optimization algorithm in ML
- **Adaptive Methods**: Modern optimizers that adjust learning rates automatically
- **Constrained Problems**: Real-world problems often have constraints (e.g., budgets, physical limits)
