import pandas as pd

data = {
    "Name": ["Noman", "Saad", "Anas", "Huzaifa", "Riaz"],
    "Age": [20, 45, 10, 52, 30],
    "Salary": [1000, 5000, 4000, 3600, 7800]
}

df = pd.DataFrame(data)

print("Averrage of Salary :", df["Salary"].mean())
print("Maximum of Salary :", df["Salary"].max())
print("Minimum of Salary :", df["Salary"].min())
print("Sum of Salary :", df["Salary"].sum())