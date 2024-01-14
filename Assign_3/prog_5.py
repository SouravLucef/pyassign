my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
sorted_disc=sorted(my_dict.values(),reverse=True)
sorted_disc=sorted_disc[:3]
print(sorted_disc)
for i in sorted_disc:
    for j in my_dict.keys():
        if my_dict[j]==i:
            print(f"{j}:{my_dict[j]}")
