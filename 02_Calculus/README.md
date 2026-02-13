# Calculus for Data Science

This directory contains implementations and examples of calculus concepts used in data science and machine learning.

## Topics Covered

### 1. Derivatives and Gradients
- Single-variable derivatives
- Partial derivatives
- Gradient vectors
- Directional derivatives

### 2. Optimization
- Gradient Descent
- Stochastic Gradient Descent (SGD)
- Mini-batch Gradient Descent
- Learning rate schedules

### 3. Backpropagation
- Chain rule
- Computational graphs
- Automatic differentiation
- Neural network training

### 4. Applications
- Loss function minimization
- Model parameter optimization
- Feature learning
- Gradient-based optimization in ML

## Files

- `derivatives.py` - Derivative computations
- `gradient_descent.py` - Gradient descent implementations
- `backprop.py` - Backpropagation from scratch
- `optimization_visualization.ipynb` - Visualizing optimization landscapes
- `neural_network_training.ipynb` - Training neural networks with calculus

## Getting Started

```python
from gradient_descent import gradient_descent

# Example: Minimize a simple function
def f(x):
    return x**2 + 5*x + 6

def df(x):
    return 2*x + 5

minimum = gradient_descent(f, df, initial_x=0, learning_rate=0.1, iterations=100)
print(f"Minimum found at: {minimum}")
```

## Key Concepts

- **Why Calculus?**: Essential for understanding how models learn and optimize
- **Gradient Descent**: The backbone of training most machine learning models
- **Chain Rule**: Enables efficient computation in deep neural networks
