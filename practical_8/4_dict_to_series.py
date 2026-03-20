# Dictionary to Pandas Series

import pandas as pd

d = {1:111, 2:222, 3:333}

print("Dictionary:", d)

s = pd.Series(d)

print("Converted to Series:")
print(s)
