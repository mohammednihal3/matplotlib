import matplotlib.pyplot as plt
 
marks = [72,93,56,78,48,98,96,76,79,85,89,79,]

plt.hist(marks, bins=5, edgecolor="black")
plt.title("Distribution of student marks")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.show()