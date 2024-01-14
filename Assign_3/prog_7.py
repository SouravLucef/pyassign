inp_str=input("Enter a string:")
print("Input String:",inp_str)
new_str=inp_str[0]
for i in range(1,len(inp_str)):
    if(inp_str[i]==inp_str[0]):
        new_str+='$'
    else:
        new_str+=inp_str[i]

print("Result String:",new_str)
