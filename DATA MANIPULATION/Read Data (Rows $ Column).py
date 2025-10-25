import pandas as pd

df = pd.read_excel("Sample.xlsx")
print("First 5 rows of the DataFrame:")
print(df.head())
print("\nLast 5 rows of the DataFrame:")
print(df.tail())