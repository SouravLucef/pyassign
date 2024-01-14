n=int(input("Enter the number of elements:"))
str_list=[]
c=0
for i in range(n):
    str=input("Enter the string: ")
    str_list.append(str)
    if(len(str)>=2 and (str[0]==str[-1])):
        c +=1


print("List :",str_list)
print("Result number :",c)