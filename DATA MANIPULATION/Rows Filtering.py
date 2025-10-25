import pandas as pd

data = {
    "Name": ["Noman", "Iqbal", "Saad", "Riaz"],
    "Age": [20, 32, 30, 20],
    "Salary": [40000, 50000, 30000, 20000]
}

df = pd.DataFrame(data)
high_salary = df[df["Salary"] > 30000]
print("Salary Greater Than 30000")
print(high_salary)

print()
print()

filter_row = df[(df["Salary"] > 30000) & (df["Age"] > 30)]
filter_or = df[(df["Salary"] > 30000) | (df["Age"] > 30)]

print(filter_row)
print(filter_or)