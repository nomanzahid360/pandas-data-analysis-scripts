import pandas as pd

# Sorting Data In 1 Column
data = {
    "Name": ["Noman", "Saad", "Anas", "Huzaifa", "Riaz"],
    "Age": [20, 45, 10, 52, 30],
    "Salary": [1000, 5000, 4000, 3600, 7800]
}

df = pd.DataFrame(data)
print("Name Column Before Sorting: ")
print(df)

df.sort_values(by="Name", ascending=True, inplace=True)
print("Name Column After Sorting: ")
print(df)
print("------------------------------------------")
# ---------------------------------------------------------------------
# Sorting Data In Multiple Columns
df.sort_values(by=["Name", "Age"], ascending=[True, False], inplace=True)
print(df)