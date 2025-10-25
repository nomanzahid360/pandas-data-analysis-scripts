import pandas as pd

# Sorting Data In 1 Column
data = {
    "Name": ["Noman", "Saad", "Anas", "Huzaifa", "Riaz"],
    "Age": [20, 45, 10, 45, 30],
    "Salary": [1000, 5000, 4000, 3600, 7800]
}

df = pd.DataFrame(data)

multi_groups = df.groupby(["Age", "Name"])["Salary"].sum()
print(multi_groups)
