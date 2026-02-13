# Data Directory

This directory contains sample datasets used in the notebooks and code examples.

## Datasets

### Sample Data
- Small datasets for demonstrations and testing
- Generated synthetic data for specific examples
- Preprocessed data for quick experimentation

## Data Guidelines

### Adding Data Files

When adding datasets:
1. Keep files small (< 10 MB when possible)
2. Use common formats (CSV, JSON, NPY)
3. Document the data source
4. Include a data dictionary if applicable

### Large Files

For large datasets:
- **Do not commit** large files to the repository
- Use `.gitignore` to exclude them
- Provide download links or scripts
- Consider using Git LFS if necessary

## Data Sources

Document your data sources here:

### Example Format
```
- dataset_name.csv
  - Source: [URL or description]
  - Description: Brief description of the data
  - Columns: List of column names and types
  - License: Data license if applicable
```

## Privacy and Ethics

- Ensure all data is properly licensed for public use
- Remove any personally identifiable information (PII)
- Credit original data sources
- Follow ethical data practices

## Note

The `.gitignore` file is configured to exclude common data file formats by default. Review it before committing data files.
