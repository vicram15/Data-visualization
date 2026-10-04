import pandas as pd

df = pd.read_csv("Healthcare_Appointments.csv")

df_20k = df.head(20000).copy()

df_20k["PatientId"] = df_20k["PatientId"].astype(str)
df_20k.to_csv("Healthcare_20000.csv", index=False)

print(df_20k.shape)
print(df_20k.head())
print("\nDataset saved successfully!")