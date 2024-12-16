import pandas as pd

# Read the CSV file with a semicolon delimiter
df = pd.read_csv('otos.csv', delimiter=';')

# Specify the column indexes you want to analyze (0-indexed)
column_indexes = [11, 12, 13, 14, 15]  # Change this to your desired indexes

for column_index in column_indexes:
    if column_index < len(df.columns):
        most_frequent = df.iloc[:, column_index].value_counts().idxmax()
        frequency = df.iloc[:, column_index].value_counts().max()

        print(f'The most frequent number in column index {column_index} is {most_frequent} (occurs {frequency} times)')
    else:
        print(f'Column index {column_index} is out of range.')