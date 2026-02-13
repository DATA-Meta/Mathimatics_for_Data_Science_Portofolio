# How to Add Your Existing Jupyter Notebooks from VS Code

This guide will help you add your existing .ipynb files from VS Code to this GitHub repository.

## Quick Steps

### 1. Copy Your Notebook Files

Copy your .ipynb files from your local VS Code workspace to the appropriate directories in this repository:

```bash
# Navigate to the repository
cd /path/to/Mathimatics_for_Data_Science_Portofolio

# Copy your notebooks to the notebooks directory
cp /path/to/your/notebooks/*.ipynb ./notebooks/

# Or organize by topic:
cp /path/to/your/linear_algebra_notebook.ipynb ./01_Linear_Algebra/
cp /path/to/your/calculus_notebook.ipynb ./02_Calculus/
# ... and so on
```

### 2. Organize by Topic

Place your notebooks in the relevant directories:

- **Linear Algebra notebooks** → `01_Linear_Algebra/`
- **Calculus notebooks** → `02_Calculus/`
- **Statistics notebooks** → `03_Probability_Statistics/`
- **Optimization notebooks** → `04_Optimization/`
- **Information Theory notebooks** → `05_Information_Theory/`
- **General/Mixed notebooks** → `notebooks/`

### 3. Using VS Code with This Repository

#### Option A: Open Repository in VS Code

1. Open VS Code
2. File → Open Folder
3. Select this repository folder: `Mathimatics_for_Data_Science_Portofolio`
4. Your notebooks will appear in the file explorer

#### Option B: Copy Files Using VS Code

1. In VS Code, open both your current workspace AND this repository
2. Drag and drop .ipynb files from one workspace to the other
3. VS Code will copy the files to the new location

### 4. Working with Notebooks in VS Code

Once your notebooks are in the repository:

1. **Install Python Extension** (if not already installed)
   - Extensions → Search "Python" → Install

2. **Install Jupyter Extension** (if not already installed)
   - Extensions → Search "Jupyter" → Install

3. **Select Python Interpreter**
   - Ctrl+Shift+P (Cmd+Shift+P on Mac)
   - Type "Python: Select Interpreter"
   - Choose the virtual environment (`venv`)

4. **Open and Run Notebooks**
   - Click on any .ipynb file
   - Click "Run All" or run cells individually
   - VS Code will render notebooks natively

### 5. Updating File Paths

If your notebooks reference data files or modules, you may need to update paths:

**Before:**
```python
import pandas as pd
data = pd.read_csv('data.csv')
```

**After (if data is in the data/ directory):**
```python
import pandas as pd
data = pd.read_csv('../data/data.csv')  # Adjust path as needed
```

**For importing custom modules:**
```python
import sys
sys.path.append('../src')  # Add src directory to path
from linear_algebra.matrix_ops import matrix_multiply
```

### 6. Add Data Files (if needed)

If your notebooks use data files:

```bash
# Copy data files
cp /path/to/your/data/*.csv ./data/
cp /path/to/your/data/*.xlsx ./data/
```

**Note:** Large data files (> 10MB) should be listed in `.gitignore` to avoid committing them to GitHub.

### 7. Test Your Notebooks

After adding notebooks:

1. Open each notebook in VS Code
2. Run all cells to ensure they work
3. Fix any import or path errors
4. Save the notebooks

### 8. Commit to GitHub

Using VS Code's Git integration:

1. **View Changes**
   - Click on Source Control icon (Ctrl+Shift+G)
   - You'll see all new .ipynb files

2. **Stage Files**
   - Click "+" next to files to stage them
   - Or click "+" next to "Changes" to stage all

3. **Commit**
   - Enter commit message: "Add master's report notebooks"
   - Click checkmark or press Ctrl+Enter

4. **Push to GitHub**
   - Click "..." → "Push"
   - Or use Terminal: `git push origin main`

## Example Directory Structure

After adding your notebooks, it might look like:

```
Mathimatics_for_Data_Science_Portofolio/
├── 01_Linear_Algebra/
│   ├── README.md
│   ├── linear_algebra_intro.ipynb
│   ├── pca_implementation.ipynb
│   └── svd_applications.ipynb
├── 02_Calculus/
│   ├── README.md
│   ├── gradient_descent.ipynb
│   └── backpropagation.ipynb
├── 03_Probability_Statistics/
│   ├── README.md
│   ├── distributions.ipynb
│   └── hypothesis_testing.ipynb
├── notebooks/
│   ├── README.md
│   ├── complete_analysis.ipynb
│   └── final_project.ipynb
└── data/
    ├── README.md
    ├── sample_data.csv
    └── results.xlsx
```

## Troubleshooting

### Issue: Notebook doesn't find Python packages

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt
```

### Issue: Notebook can't import custom modules

**Solution:** Add this at the top of your notebook:
```python
import sys
import os
sys.path.append(os.path.abspath('../src'))
```

### Issue: Data files not found

**Solution:** Use relative paths or absolute paths:
```python
# Relative path (recommended)
data_path = '../data/myfile.csv'

# Or use os.path
import os
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'myfile.csv')
```

## Using Terminal in VS Code

You can also use the integrated terminal in VS Code:

1. **Open Terminal**: Ctrl+` (backtick) or View → Terminal
2. **Navigate**: `cd Mathimatics_for_Data_Science_Portofolio`
3. **Copy files**: `cp ../old_location/*.ipynb ./notebooks/`
4. **Check status**: `git status`
5. **Add files**: `git add .`
6. **Commit**: `git commit -m "Add notebooks"`
7. **Push**: `git push`

## Best Practices

1. **Organize notebooks logically** by topic
2. **Use descriptive filenames** (e.g., `01_matrix_operations.ipynb` not `notebook1.ipynb`)
3. **Clear outputs before committing** (optional but recommended for clean diffs)
4. **Add markdown cells** to explain your work
5. **Keep notebooks focused** - one concept per notebook when possible
6. **Test after copying** to ensure everything works

## Need Help?

- Check GETTING_STARTED.md for setup instructions
- Review CONTRIBUTING.md for coding standards
- Open an issue if you encounter problems

---

**Ready to publish your work? Start by copying your notebooks into the appropriate directories!**
