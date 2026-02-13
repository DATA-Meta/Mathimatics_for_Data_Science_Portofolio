# Probability and Statistics for Data Science

This directory contains implementations and examples of probability and statistical concepts for data science.

## Topics Covered

### 1. Probability Fundamentals
- Probability distributions (Normal, Binomial, Poisson, etc.)
- Joint and conditional probability
- Bayes' Theorem
- Random variables and expectations

### 2. Descriptive Statistics
- Measures of central tendency (mean, median, mode)
- Measures of dispersion (variance, standard deviation)
- Correlation and covariance
- Data visualization

### 3. Inferential Statistics
- Confidence intervals
- Hypothesis testing (t-tests, chi-square, ANOVA)
- p-values and significance levels
- A/B testing

### 4. Bayesian Statistics
- Prior and posterior distributions
- Bayesian inference
- Maximum A Posteriori (MAP) estimation
- Bayesian networks

### 5. Applications
- Statistical modeling
- Uncertainty quantification
- Feature selection
- Model evaluation

## Files

- `distributions.py` - Probability distribution implementations
- `descriptive_stats.py` - Descriptive statistics functions
- `hypothesis_testing.py` - Hypothesis testing implementations
- `bayesian_inference.ipynb` - Bayesian methods examples
- `ab_testing.ipynb` - A/B testing case study

## Getting Started

```python
import numpy as np
from distributions import normal_distribution
from hypothesis_testing import t_test

# Example: Normal distribution sampling
samples = normal_distribution(mean=0, std=1, size=1000)

# Example: Hypothesis testing
group_a = np.random.normal(100, 15, 50)
group_b = np.random.normal(105, 15, 50)
result = t_test(group_a, group_b)
print(f"t-statistic: {result['t_stat']}, p-value: {result['p_value']}")
```

## Key Concepts

- **Why Probability & Statistics?**: Foundation for understanding data, uncertainty, and making inferences
- **Distributions**: Model real-world phenomena and understand data patterns
- **Hypothesis Testing**: Make data-driven decisions with statistical rigor
- **Bayesian Methods**: Incorporate prior knowledge and update beliefs with data
