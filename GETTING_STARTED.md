# Getting Started Guide

Welcome to the Mathematics for Data Science Portfolio! This guide will help you get started with the repository.

## Quick Start

### 1. Prerequisites

Before you begin, ensure you have:
- Python 3.8+ installed
- Git installed
- A code editor (VS Code recommended)
- Basic knowledge of Python and mathematics

### 2. Installation

**Clone the repository:**
```bash
git clone https://github.com/DATA-Meta/Mathimatics_for_Data_Science_Portofolio.git
cd Mathimatics_for_Data_Science_Portofolio
```

**Create a virtual environment:**
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

### 3. Explore the Repository

**Directory Structure:**
```
Mathimatics_for_Data_Science_Portofolio/
├── 01_Linear_Algebra/          # Linear algebra concepts
├── 02_Calculus/                # Calculus for ML
├── 03_Probability_Statistics/  # Probability & Statistics
├── 04_Optimization/            # Optimization algorithms
├── 05_Information_Theory/      # Information theory
├── notebooks/                  # Jupyter notebooks
├── src/                        # Source code modules
├── data/                       # Sample datasets
└── reports/                    # Master's report
```

### 4. Run Your First Notebook

**Start Jupyter:**
```bash
jupyter notebook
```

**Navigate to `notebooks/` and open any notebook to explore!**

### 5. Using the Code Modules

**Example - Linear Algebra:**
```python
import numpy as np
import sys
sys.path.append('./src')

# Your code here
from linear_algebra.matrix_ops import matrix_multiply

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = matrix_multiply(A, B)
print(C)
```

## Learning Path

### For Beginners

1. Start with **Linear Algebra basics**
   - Vectors and matrices
   - Matrix operations
   - Eigenvalues

2. Move to **Calculus fundamentals**
   - Derivatives
   - Gradients
   - Optimization

3. Learn **Probability & Statistics**
   - Distributions
   - Statistical testing
   - Bayesian thinking

### For Intermediate Learners

1. Deep dive into **Optimization**
   - Gradient descent variants
   - Advanced optimizers
   - Constrained optimization

2. Explore **Information Theory**
   - Entropy
   - Cross-entropy loss
   - Mutual information

3. Work through **real-world applications**
   - PCA for dimensionality reduction
   - Building neural networks
   - Statistical modeling

## Working with VS Code

### Recommended Extensions

1. **Python** - Microsoft
2. **Jupyter** - Microsoft
3. **Python Docstring Generator** - Nils Werner
4. **GitLens** - GitKraken
5. **Markdown All in One** - Yu Zhang

### VS Code Setup

1. Open the repository folder in VS Code
2. Select your Python interpreter (from venv)
3. Install recommended extensions
4. You can now edit code and run notebooks directly in VS Code!

## Tips for Success

### 1. Hands-On Practice
- Don't just read - code along!
- Modify examples and see what happens
- Try different parameters

### 2. Mathematics Review
- Review mathematical concepts as needed
- Use external resources (Khan Academy, 3Blue1Brown)
- Focus on intuition, not just formulas

### 3. Build Projects
- Apply concepts to real datasets
- Create your own notebooks
- Share your work!

### 4. Documentation
- Read the README files in each directory
- Check inline comments and docstrings
- Review the master's report in `reports/`

## Common Issues

### Issue: Module not found
**Solution:** Make sure you're in the correct directory and have activated the virtual environment

### Issue: Jupyter kernel not found
**Solution:** 
```bash
python -m ipykernel install --user --name=venv
```

### Issue: Import errors in notebooks
**Solution:** Add the src directory to your Python path:
```python
import sys
sys.path.append('../src')
```

## Next Steps

1. ✅ Complete the installation
2. ✅ Run a sample notebook
3. ✅ Explore the code modules
4. 📚 Read the topic-specific READMEs
5. 🧪 Try modifying examples
6. 🚀 Create your own implementations

## Resources

### Mathematical Foundations
- [Khan Academy](https://www.khanacademy.org/) - Free math courses
- [3Blue1Brown](https://www.youtube.com/c/3blue1brown) - Visual math explanations
- [MIT OpenCourseWare](https://ocw.mit.edu/) - Free course materials

### Python & Data Science
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

### Books
- "Mathematics for Machine Learning" by Deisenroth, Faisal, and Ong
- "Pattern Recognition and Machine Learning" by Bishop
- "The Elements of Statistical Learning" by Hastie, Tibshirani, and Friedman

## Getting Help

- 📖 Check the documentation in each directory
- 💬 Open an issue on GitHub
- 🔍 Search existing issues
- 📧 Contact the repository owner

## Contributing

Interested in contributing? Check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines!

---

**Happy Learning! 📊🔢🎓**
