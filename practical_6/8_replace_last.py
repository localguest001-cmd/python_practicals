# Replace last value of tuples in list

my_list = [(1,2,3),(4,5,6),(7,8,9)]

new_list = []

for tpl in my_list:
    new_tpl = tpl[:-1] + (100,)
    new_list.append(new_tpl)

print("The new list is:", new_list)
