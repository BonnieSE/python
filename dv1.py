import matplotlib.pyplot as plt

a = (1,4,9,16,25)
plt.plot(a, linewidth = 5)

plt.title("a", fontsize =20)
plt.xlabel("time", fontsize = 15)
plt.ylabel("value", fontsize = 15)

plt.tick_params(axis = 'both', labelsize = 20)
plt.show()

# Coorecting the plot
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
plt.show()

plt.scatter(2, 4, s=200)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
plt.show()

# Removing Outlines from Data Points
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, edgecolor='none', s=20)
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=20)
plt.scatter(x_values, y_values, c=(1, 0, 0.9), edgecolor='none', s=40)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])
plt.show()

# Using a colormap
x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.show()



