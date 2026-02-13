# Quick Reference: Publishing Your VS Code Notebooks to GitHub

## Step-by-Step Checklist

### ✅ Step 1: Prepare Your Environment
```bash
# Clone or navigate to repository
cd Mathimatics_for_Data_Science_Portofolio

# Create virtual environment (if not done)
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### ✅ Step 2: Add Your Notebooks

**Option 1: Using File Explorer**
- Copy your .ipynb files from your current location
- Paste them into the appropriate directories in this repository

**Option 2: Using VS Code**
- Open this repository folder in VS Code
- Drag and drop your .ipynb files into the desired folders
- Or use VS Code's file menu to copy/move files

**Option 3: Using Terminal/Command Line**
```bash
# Copy all notebooks from your current location
cp /path/to/your/notebooks/*.ipynb ./notebooks/

# Or copy to specific topic folders
cp path/to/linear_algebra.ipynb ./01_Linear_Algebra/
cp path/to/calculus.ipynb ./02_Calculus/
```

### ✅ Step 3: Organize by Topic

Place notebooks in the right folders:
- `01_Linear_Algebra/` - Linear algebra topics
- `02_Calculus/` - Calculus and derivatives  
- `03_Probability_Statistics/` - Probability and statistics
- `04_Optimization/` - Optimization algorithms
- `05_Information_Theory/` - Entropy, KL divergence, etc.
- `notebooks/` - Mixed or general notebooks
- `reports/` - Final report documents (PDFs, etc.)

### ✅ Step 4: Add Your Data Files (if any)
```bash
# Copy data files to data directory
cp /path/to/your/data/*.csv ./data/
cp /path/to/your/data/*.xlsx ./data/
```

**Important:** Check `.gitignore` - large files (>10MB) won't be committed automatically.

### ✅ Step 5: Fix Import Paths

Update paths in your notebooks if needed:

```python
# Add this at the top of notebooks to import from src/
import sys
sys.path.append('../src')

# Then you can import custom modules
from linear_algebra.matrix_ops import matrix_multiply

# For data files, use relative paths
import pandas as pd
data = pd.read_csv('../data/your_data.csv')
```

### ✅ Step 6: Test Your Notebooks

Open notebooks in VS Code and run them:
1. Click on .ipynb file
2. Select Python kernel (from venv)
3. Run all cells
4. Fix any errors

### ✅ Step 7: Commit and Push to GitHub

**Using VS Code:**
1. Open Source Control (Ctrl+Shift+G)
2. Review changed files
3. Stage files (click +)
4. Write commit message: "Add master's report notebooks"
5. Commit (click ✓)
6. Push to GitHub

**Using Terminal:**
```bash
# Check what's changed
git status

# Add all new files
git add .

# Commit with message
git commit -m "Add master's report notebooks and data"

# Push to GitHub
git push origin main
```

### ✅ Step 8: Verify on GitHub

1. Go to your GitHub repository
2. Check that files are uploaded
3. View notebooks directly on GitHub (GitHub renders .ipynb files!)

## Common File Locations

Where to put your files:

| Your File Type | Put It Here | Example |
|---------------|-------------|---------|
| Linear algebra notebook | `01_Linear_Algebra/` | `matrix_operations.ipynb` |
| Calculus notebook | `02_Calculus/` | `gradient_descent.ipynb` |
| Statistics notebook | `03_Probability_Statistics/` | `hypothesis_testing.ipynb` |
| Any other notebook | `notebooks/` | `complete_analysis.ipynb` |
| CSV/Excel data | `data/` | `dataset.csv` |
| PDF report | `reports/` | `masters_report.pdf` |
| Python scripts | `src/[topic]/` | `src/linear_algebra/pca.py` |

## VS Code Extensions You Need

Install these in VS Code:
1. **Python** (by Microsoft)
2. **Jupyter** (by Microsoft)
3. **Pylance** (by Microsoft) - for better Python support

## Quick Commands Reference

```bash
# Navigate to repository
cd Mathimatics_for_Data_Science_Portofolio

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install/Update packages
pip install -r requirements.txt

# Check Git status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log --oneline

# Create new branch (if needed)
git checkout -b my-new-branch
```

## Help & Documentation

- **Full guide**: See `ADD_YOUR_NOTEBOOKS.md`
- **Getting started**: See `GETTING_STARTED.md`
- **Contributing**: See `CONTRIBUTING.md`
- **Main README**: See `README.md`

## Need Help?

If you encounter issues:
1. Check the detailed guides above
2. Search for error messages online
3. Open an issue on GitHub
4. Check VS Code's Output panel for errors

---

**🎉 You're ready to publish your master's report code to GitHub!**
