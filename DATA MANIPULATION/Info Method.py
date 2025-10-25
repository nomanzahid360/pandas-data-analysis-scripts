"""
How to get Info of a DataFrame in Pandas:
Total number of rows and columns
Column names
Data types of each column
Non-null counts
Storage memory usage
"""
import pandas as pd

# With Big DataFrame
df = pd.read_excel("Sample.xlsx")
print("DataFrame Info:")
print(df.info())

# With Small DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
small_df = pd.DataFrame(data)
print("\nSmall DataFrame Info:")
print(small_df.info())
