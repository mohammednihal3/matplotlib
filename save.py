import matplotlib.pyplot  as plt

months = ["Jan", "Feb", "March", "April", "May"]
sales = [120, 150, 135, 170, 210]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.savefig("monthly_sales.png", dpi=300, bbox_inches="tight")
plt.show()