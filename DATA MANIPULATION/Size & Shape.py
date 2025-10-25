import pandas as pd

df = pd.read_excel("Sample.xlsx")

print(f"Shape of the DataFrame: {df.shape}")
print(f"Columns Names in the DataFrame: \n{df.columns}")