# Pie chart

import matplotlib.pyplot as plt

medal = [50,46,27,26,19,17]
country = ["INDIA","US","BRITAIN","CHINA","RUSSIA","GERMANY"]

plt.figure(figsize=(7,7))

plt.title("Gold medal achievements")

plt.pie(medal, labels=country, autopct='%0.2f%%')

plt.show()
