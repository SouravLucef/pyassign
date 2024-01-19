def extract_name(inp_email):
    indx=inp_email.index('@')
    name=""
    for i in inp_email.lower():
        if i=='@':
            break
        elif i>='a' and i<='z':
            name+=i
    return name
inp_email=input("Enter email address:")
print("Required Name:",extract_name(inp_email))