import matplotlib.pyplot as plt
months = ["Jan", "Feb", "March", "April", "May"]
sales = [120, 150, 135, 170, 210]

plt.plot(months, sales)
plt.title("Monthly sales")
plt.xlabel("Month")
plt.ylabel("Sales(units)")
plt.show()