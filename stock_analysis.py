import pandas as pd
import matplotlib.pyplot as plt

# Load the spreadsheet
file_path = 'stock_data.xlsx'  # Update this path if necessary
data = pd.read_excel(file_path)

# Display the data
print(data)

# Calculate Gain/Loss percentage
data['G/L %'] = (data['Price'] - data['BOUGHT FOR']) / data['BOUGHT FOR'] * 100

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(data['TITLE'], data['G/L %'], color='blue')
plt.xlabel('Stock Title')
plt.ylabel('Gain/Loss Percentage (%)')
plt.title('Stock Gain/Loss Percentage')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()
