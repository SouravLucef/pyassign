disc={}

while key1:=input("Enter ker or press enter to exit:"):
    listofelem=input("Enter comma seperated elements: ").split(',')
    disc[key1]=listofelem
    with open (f"{key1}.txt","w") as f:
        for i in listofelem:
            f.write(f"{i}\n")
print(disc)