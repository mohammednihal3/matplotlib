import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
plt.plot(df["Month"], df["Revenue"], marker="o")
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()