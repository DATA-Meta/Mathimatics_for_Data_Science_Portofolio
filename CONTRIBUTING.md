# Contributing to Mathematics for Data Science Portfolio

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the issue tracker
2. If not, create a new issue with:
   - A clear title
   - Detailed description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior

### Contributing Code

1. **Fork the repository**
   ```bash
   git clone https://github.com/DATA-Meta/Mathimatics_for_Data_Science_Portofolio.git
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clear, commented code
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation

4. **Test your changes**
   ```bash
   python -m pytest tests/
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide a clear description
   - Reference any related issues
   - Wait for review

## Code Style

### Python Code

- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings to all functions
- Keep functions focused and modular

Example:
```python
def compute_entropy(probabilities):
    """
    Compute Shannon entropy of a probability distribution.
    
    Args:
        probabilities (numpy.ndarray): Array of probabilities
        
    Returns:
        float: Entropy value
        
    Example:
        >>> probs = np.array([0.5, 0.3, 0.2])
        >>> compute_entropy(probs)
        1.0296530140645737
    """
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))
```

### Jupyter Notebooks

- Clear markdown explanations
- Well-commented code cells
- Include visualizations
- Show expected outputs

### Documentation

- Use clear, concise language
- Include code examples
- Keep README files updated
- Add mathematical formulas where relevant (using LaTeX)

## Mathematical Notation

When documenting mathematical concepts, use LaTeX notation:

- Inline: `$f(x) = x^2$`
- Block: 
  ```latex
  $$
  \nabla f(x) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \end{bmatrix}
  $$
  ```

## Adding New Topics

When adding a new mathematical topic:

1. Create a new directory if needed
2. Add a comprehensive README.md
3. Include code implementations
4. Add Jupyter notebook examples
5. Update the main README.md
6. Add references to reports/

## Testing

- Add unit tests for new functions
- Ensure all tests pass before submitting
- Test notebooks (run all cells)
- Check that examples work

## Questions?

Feel free to open an issue for any questions or discussions!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
