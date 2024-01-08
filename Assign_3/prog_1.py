n=int(input("Enter the number of elements:"))
str_list=[]
c=0
for i in range(n):
    sr=input("Enter the string: ")
    str_list.append(sr)
    if(len(sr)>=2 and (sr[0]==sr[-1])):
        c +=1

print("List :",str_list)
print("Result number :",c)