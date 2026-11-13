import matplotlib.pyplot as plt

products = ["Tablets", "Laptops", "Mobiles","Watch"]
units_sold = [35, 65, 20, 12]

plt.barh(products, units_sold, color="seagreen")
plt.title("Product Sales Comparison")
plt.xlabel("Units Sold")
plt.show()