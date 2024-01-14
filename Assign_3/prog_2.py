tu_list=[]

n=int(input("Enter the list length: "))
for i in range(n):
    mytuple=tuple(int(x) for x in (input("Enter space seperated numbers:").split()))
    tu_list.append(mytuple)
print(f"Given list: {tu_list}")
print(f"Sorted List:{sorted(tu_list,key=lambda elem: elem[-1])}")
