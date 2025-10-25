import pandas as pd
data = {
    "Name": ["Noman", "Iqbal", "Saad", "Riaz"],
    "Age":[20, 32, 30, 20],
    "Salary":[40000, 50000, 30000, 20000]
}

df = pd.DataFrame(data)

name_column = df["Name"]
print("Before", name_column[0])

name_column[0] = "Muhammad Noman Zahid"
print("After", name_column[0])
