with open('fiel1.txt','w') as f:
    print("Enter your text--")
    while inp_text:=input("->"):
        f.write(f"{inp_text}\n")
    
with open('fiel1.txt','r') as f:
    text=f.readlines()

print(text)