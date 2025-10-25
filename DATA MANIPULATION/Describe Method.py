import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Salary": [50000, 60000, 55000, 70000, 65000]
}

df = pd.DataFrame(data)
print(df.describe())

print(df.shape)
print(df.columns)