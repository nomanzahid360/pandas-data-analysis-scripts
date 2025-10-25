import pandas as pd

random_data = {
    "Name": [
        "Noman", "Iqbal", "Saad", "Riaz", "Shah Nawaz", "Huzaifa", "Haseeb",
        "Hassan", "Osman", "Orhan"
    ],
    "Age": [44, 40, None, 80, None, 22, 74, 88, None, 65]
}

df = pd.DataFrame(random_data)

print("Before Linear InterPolation")
print(df)
print("\n\n")
df["Age"] = df["Age"].interpolate(method="linear")
print("After Linear InterPolation")
print(df)
