
my_list=input("Enther the elements as space seperated:").split()
new_list=[]
for i in my_list:
    if(i not in new_list):
        new_list.append(i)
        print(f"No. of {i} in List is {my_list.count(i)}")
print(my_list)
print(new_list)