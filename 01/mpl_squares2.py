import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.style.use(['dark_background'])
plt.plot(squares, linewidth=5)
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.xlabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()