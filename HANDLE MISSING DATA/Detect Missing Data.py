import pandas as pd

class_data = {}

df = pd.DataFrame(class_data)

# Add AG No
df.insert(0, "AG No", [
    None, "2023-ag-8151", "2023-ag-8152", "2023-ag-8153",
    "2023-ag-8154", "2023-ag-8155", "2023-ag-8156", "2023-ag-8157",
    "2023-ag-8158", "2023-ag-8159", "2023-ag-8160"
])

# Add Names
df.insert(1, "Name", [
    "Huzaifa", "Ali Hassan", "Noman Zahid", "Hassan Raza", "Riaz Hussain",
    "Haseeb Hassan", "Talha Fahad", "Tayyab", "Samiullah", "Rohail Amjad",
    "Saad Farooq"
])

# Add Attendence_Percentage at Last
df["Attendence_Percentage"] = [
    "20%", "40%", "60%", "65%", "70%", "75%", "80%", "82%", "85%", "90%", "99%"
]
# --------------

print(df.isnull())

# Count Missing Data
print(df.isnull().sum())
