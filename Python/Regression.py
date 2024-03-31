import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Given data
data = {
    'Years': list(range(2010, 2020)),
    'Canada (CAD)': [1666048, 1774063, 1827201, 1902247, 1994898, 1990441, 2025535, 2140641, 2231168, 2310712],
    'China (Yuan)': [40850539.91, 48410930.60, 53903990.60, 59634448.16, 64654796.07, 69209369.91, 74598050.82, 82898276.40, 91577425.51, 99492740.00],
    'China (In CAD)': [7761602.58, 9198076.81, 10241758.21, 11330545.15, 12284411.25, 13149780.28, 14173629.66, 15750672.52, 17399710.85, 18903620.60]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Perform regression analysis for Canada
X_canada = sm.add_constant(df['Years'])
y_canada = df['Canada (CAD)']

model_canada = sm.OLS(y_canada, X_canada)
results_canada = model_canada.fit()
print("Regression Results for Canada:")
print(results_canada.summary())

# Perform regression analysis for China
X_china = sm.add_constant(df['Years'])
y_china = df['China (In CAD)']  # Using China (In CAD) as dependent variable for China

model_china = sm.OLS(y_china, X_china)
results_china = model_china.fit()
print("\nRegression Results for China:")
print(results_china.summary())
