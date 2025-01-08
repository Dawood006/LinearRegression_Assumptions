# Linear Assumption Verification Toolkit

This repository contains a Python module and an example notebook for verifying key assumptions of linear regression. These tools are designed to assist data analysts and scientists in evaluating the validity of their data for linear regression modeling.

## Contents

1. **`L_assumption.py`**  
   This file contains the `Assumption` class, which provides various functions to check linear regression assumptions.

2. **`Linear_Assumption.ipynb`**  
   An interactive Jupyter notebook demonstrating the usage of the `Assumption` class with real-world datasets.

---

## Features of the `Assumption` Class

The `Assumption` class offers the following functionalities:

1. **Linear Relationship Check**
   - Visualizes scatter plots between independent variables and the target variable to evaluate linear relationships.

2. **Correlation Matrix**
   - Generates a heatmap to visualize correlation coefficients between features.

3. **Homoscedasticity Check**
   - Plots residuals versus predicted values to assess constant variance.

4. **Normality of Residuals**
   - Produces a Q-Q plot and density plot for the residuals to evaluate normal distribution.

5. **Normality of Features**
   - Creates Q-Q plots for each feature to assess their normality.

6. **Autocorrelation of Residuals**
   - Visualizes residuals to identify any autocorrelation patterns.

---

## Usage Instructions

### Prerequisites

- Python 3.8 or later
- Required libraries:
  - `pandas`
  - `numpy`
  - `seaborn`
  - `matplotlib`
  - `scipy`

Install the required dependencies using:

```bash
pip install pandas numpy seaborn matplotlib scipy
```

### Running the Example Notebook

1. Clone this repository:

   ```bash
   git clone https://github.com/Dawood006/LinearRegression_Assumptions.git
   ```

2. Navigate to the project directory:

   ```bash
   cd LinearRegression_Assumptions
   ```

3. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

4. Open `Linear_Assumption.ipynb` to explore the usage of the `Assumption` class.

---

