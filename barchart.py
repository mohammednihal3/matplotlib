import matplotlib.pyplot as plt
products = ["Tablets", "Laptops", "Mobiles","Watch"]
units_sold = [35, 65, 20, 12]

plt.bar(products, units_sold, color="steelblue")
plt.title("Unit sold by products")
plt.xlabel("Product")
plt.ylabel("Units_sold")
plt.show()