inp_str=input("Enter a String :").lower()
str1=''
str2=''
for i in inp_str:
    if inp_str.count(i)==1:
        str1+=i
    elif inp_str.count(i)>1 and i not in str2:
        str2+=i
print("String of single character occurence:",str1)
print("String of multiple character occurence:",str2)