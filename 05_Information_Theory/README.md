# Information Theory for Data Science

This directory contains implementations and examples of information theory concepts used in data science and machine learning.

## Topics Covered

### 1. Entropy
- Shannon Entropy
- Joint and Conditional Entropy
- Entropy in data compression
- Maximum entropy principle

### 2. Cross-Entropy and KL Divergence
- Cross-Entropy loss
- Kullback-Leibler (KL) Divergence
- Jensen-Shannon Divergence
- Applications in model training

### 3. Mutual Information
- Mutual Information computation
- Feature selection using MI
- Information gain
- Decision trees

### 4. Applications in Machine Learning
- Loss functions (Cross-Entropy Loss)
- Model evaluation
- Feature selection
- Generative models (VAEs, GANs)
- Information bottleneck theory

## Files

- `entropy.py` - Entropy and related measures
- `divergences.py` - KL divergence and other divergence measures
- `mutual_information.py` - Mutual information computations
- `loss_functions.ipynb` - Information-theoretic loss functions
- `feature_selection.ipynb` - Feature selection using MI

## Getting Started

```python
from entropy import shannon_entropy, cross_entropy
from divergences import kl_divergence
import numpy as np

# Example: Computing entropy
p = np.array([0.5, 0.3, 0.2])
H = shannon_entropy(p)
print(f"Entropy: {H}")

# Example: KL divergence
q = np.array([0.4, 0.4, 0.2])
kl_div = kl_divergence(p, q)
print(f"KL Divergence: {kl_div}")
```

## Key Concepts

- **Entropy**: Measures uncertainty or information content in data
- **Cross-Entropy**: Standard loss function for classification problems
- **KL Divergence**: Measures how one distribution differs from another
- **Mutual Information**: Quantifies dependency between variables, useful for feature selection

## Mathematical Foundations

### Shannon Entropy
```
H(X) = -∑ p(x) log p(x)
```

### Cross-Entropy
```
H(p, q) = -∑ p(x) log q(x)
```

### KL Divergence
```
D_KL(p || q) = ∑ p(x) log(p(x) / q(x))
```

### Mutual Information
```
I(X; Y) = H(X) + H(Y) - H(X, Y)
```
