"my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}"

def highest_three_value(my_dict):
    sorted_disc=sorted(my_dict.values(),reverse=True)
    sorted_disc=sorted_disc[:3]
    print(sorted_disc)
    for i in sorted_disc:
        for j in my_dict.keys():
            if my_dict[j]==i:
                print(f"{j}:{my_dict[j]}")


my_dict={}
n=int(input("Enter the Length of dictionary greater than 3 :")) 
if n > 3 :
    for i in range(n):
        dkey=input("Enter Key:")
        my_dict[dkey]=int(input(f"Enter value for {dkey}:"))
    highest_three_value(my_dict)
else:
    print("Enter a correct Length!")




