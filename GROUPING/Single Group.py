import pandas as pd

# Sorting Data In 1 Column
data = {
    "Name": ["Noman", "Saad", "Anas", "Huzaifa", "Riaz"],
    "Age": [20, 45, 10, 20, 30],
    "Salary": [1000, 5000, 4000, 3600, 7800]
}

df = pd.DataFrame(data)

single_group = df.groupby("Age")["Salary"].sum()
print(single_group)