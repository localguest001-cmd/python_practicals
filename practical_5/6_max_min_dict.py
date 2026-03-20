# Max and Min in dictionary

my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 3}

max_value = max(my_dict.values())
max_key = max(my_dict, key=my_dict.get)

min_value = min(my_dict.values())
min_key = min(my_dict, key=my_dict.get)

print("Maximum value:", max_value, "Key:", max_key)
print("Minimum value:", min_value, "Key:", min_key)
