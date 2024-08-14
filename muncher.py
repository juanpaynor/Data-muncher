import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Jane', 'Doe'],
    'Age': [30, 25, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
