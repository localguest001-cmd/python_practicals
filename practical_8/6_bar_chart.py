# Bar chart (Vertical + Horizontal)

import matplotlib.pyplot as plt

languages = ["JAVA","PYTHON","PHP","JAVASCRIPT","C#","C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Vertical
plt.bar(languages, popularity)
plt.title("Vertical Bar Chart")
plt.xlabel("Languages")
plt.ylabel("Popularity")

for i in range(len(languages)):
    plt.text(i, popularity[i], str(popularity[i]))

plt.show()

# Horizontal
plt.barh(languages, popularity)
plt.title("Horizontal Bar Chart")
plt.xlabel("Popularity")
plt.ylabel("Languages")

plt.show()
