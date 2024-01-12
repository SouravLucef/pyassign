my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
# x=reversed(my_dict.items())
# print(x)'
for k,v in reversed(my_dict.items()):
    print(k,v)

x=sorted(my_dict.values())
print(x)