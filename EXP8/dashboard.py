import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Financial_20000.csv")
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df[df["Quantity"] > 0]

revenue = df["TotalSales"].sum()
orders = df["InvoiceNo"].nunique()

fig, ax = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("ONLINE RETAIL SALES DASHBOARD", fontsize=20, fontweight="bold")

# Monthly Sales
monthly = df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalSales"].sum()
ax[0,0].plot(monthly.astype(str), monthly.values, marker="o")
ax[0,0].set_title("Monthly Sales Trend")
ax[0,0].tick_params(axis="x", rotation=45)

# Top Countries
country = df.groupby("Country")["TotalSales"].sum().nlargest(5)
ax[0,1].bar(country.index, country.values)
ax[0,1].set_title("Top 5 Countries by Sales")
ax[0,1].tick_params(axis="x", rotation=30)

# Top Products
products = df.groupby("Description")["TotalSales"].sum().nlargest(5)
ax[1,0].barh(products.index, products.values)
ax[1,0].set_title("Top 5 Products by Revenue")

# KPI
ax[1,1].axis("off")
ax[1,1].text(0.1, 0.65, f"TOTAL REVENUE\n£{revenue:,.0f}", fontsize=22, fontweight="bold")
ax[1,1].text(0.1, 0.25, f"TOTAL ORDERS\n{orders:,}", fontsize=22, fontweight="bold")

plt.tight_layout()
plt.savefig("Retail_Dashboard.png", dpi=200)
plt.show()