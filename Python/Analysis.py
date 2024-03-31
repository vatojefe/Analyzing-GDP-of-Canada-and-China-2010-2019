import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Years': list(range(2010, 2020)),
    'Canada (CAD)': [1666048, 1774063, 1827201, 1902247, 1994898, 1990441, 2025535, 2140641, 2231168, 2310712],
    'China (Yuan)': [40850539.91, 48410930.60, 53903990.60, 59634448.16, 64654796.07, 69209369.91, 74598050.82, 82898276.40, 91577425.51, 99492740.00],
    'China (In CAD)': [7761602.58, 9198076.81, 10241758.21, 11330545.15, 12284411.25, 13149780.28, 14173629.66, 15750672.52, 17399710.85, 18903620.60]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Calculate mean, mode, and standard deviation
mean_values = df.mean()
mode_values = df.mode().iloc[0]
std_values = df.std()

# Print mean, mode, and standard deviation
print("Mean:")
print(mean_values)
print("\nMode:")
print(mode_values)
print("\nStandard Deviation:")
print(std_values)

# Plot line graph
plt.figure(figsize=(10, 5))
plt.plot(df['Years'], df['Canada (CAD)'], marker='o', label='Canada (CAD)')
plt.plot(df['Years'], df['China (Yuan)'], marker='o', label='China (Yuan)')
plt.plot(df['Years'], df['China (In CAD)'], marker='o', label='China (In CAD)')
plt.xlabel('Years')
plt.ylabel('Amount')
plt.title('Line Graph')
plt.legend()
plt.grid(True)
plt.show()

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(df['Years'], df['Canada (CAD)'], label='Canada (CAD)')
plt.bar(df['Years'], df['China (Yuan)'], label='China (Yuan)')
plt.bar(df['Years'], df['China (In CAD)'], label='China (In CAD)')
plt.xlabel('Years')
plt.ylabel('Amount')
plt.title('Bar Chart')
plt.legend()
plt.show()

# Plot Pareto chart
sorted_df = df.sort_values(by='Canada (CAD)', ascending=False)
cumulative_percentage = sorted_df['Canada (CAD)'].cumsum() / sorted_df['Canada (CAD)'].sum() * 100

fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.bar(df['Years'], df['Canada (CAD)'], color='b')
ax1.set_ylabel('Canada (CAD)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(df['Years'], cumulative_percentage, color='r', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage', color='r')
ax2.tick_params('y', colors='r')

plt.title('Pareto Chart')
plt.legend()
plt.show()
