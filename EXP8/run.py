import pandas as pd

df = pd.read_excel("Online_Retail.xlsx")

df = df.dropna(subset=["CustomerID"])
df = df[df["Quantity"] > 0].head(20000)

df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

df.to_csv("Financial_20000.csv", index=False)

print("Dataset Shape:", df.shape)
print(df.head())
print("Dataset Created Successfully")