# World Happiness Report 2021 Analysis

This project analyzes the **World Happiness Report 2021** dataset using Python and NumPy. It explores the factors contributing to happiness across different countries and regions.

## Project Structure

- **`happiness_project.ipynb`**: A Jupyter Notebook containing the step-by-step analysis, codes, and explanations.
- **`run_analysis.py`**: A Python script that executes the analysis logic and prints the results.
- **`world-happiness-report-2021.csv`**: The dataset used for this analysis.
- **`final_output.txt`**: A text file containing the output results of the analysis script.

## Key Features

The analysis covers the following aspects:
1.  **Data Loading**: handling CSV data with mixed types and encodings.
2.  **Basic Statistics**: calculating mean, median, and standard deviation of happiness scores.
3.  **Rankings**: Identifying the top 10 happiest and bottom 10 least happy countries.
4.  **Regional Analysis**: Comparing average happiness scores across different global regions.
5.  **Correlations**: Analyzing the relationship between happiness and factors like GDP, Social Support, Life Expectancy, Freedom, Generosity, and Corruption.

## How to Run

### Using Python Script
You can run the analysis directly from the terminal:
```bash
python run_analysis.py
```
This will generate the analysis and print it to `final_output.txt`.

### Using Jupyter Notebook
Open `happiness_project.ipynb` in Jupyter Notebook or VS Code and run all cells to visually step through the analysis.

## Requirements
- Python 3.x
- NumPy
- Matplotlib (imported in notebook for potential future plotting)
