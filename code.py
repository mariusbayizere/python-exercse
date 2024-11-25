import matplotlib.pyplot as plt

x_values: list[int] = [1, 2, 3, 4, 5]
y_values: list[int] = [2, 3, 5, 7, 11]


plt.bar(x_values, y_values)
plt.title('This chat show as the information about the chat')
plt.xlabel('Category X')
plt.ylabel('Category Y')
plt.show()