import pandas as pd

students_Data = {
    "Name": ["Noman", "Huzaifa", "Riaz", "Shah Nawaz", "Shan"],
    "Ag_No": [8165, 8150, 8187, 8189, 8120],
    "City": ["Gojra", "Sargodha", "Chiniot", "Okara", "Jhang"]
}

df = pd.DataFrame(students_Data)
# print(df)
# df.to_csv("D:\Coding\PANDAS LIBRARY\PANDAS\Save Data\Students Data.csv", index=False)
# df.to_excel("Students Data.xlsx", index=False)
# df.to_json("D:\Coding\PANDAS LIBRARY\PANDAS\Save Data\Students Data.json", index=False)
df.to_html("D:\Coding\PANDAS LIBRARY\PANDAS\Save Data\Students Data.html", index=False)
