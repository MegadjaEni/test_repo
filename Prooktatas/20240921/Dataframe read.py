
import pandas as pd

# Read the CSV file
df = pd.read_csv('otos.csv', delimiter=';')

# Print the DataFrame and its columns
print(df)
print("Columns in DataFrame:", df.columns.tolist())