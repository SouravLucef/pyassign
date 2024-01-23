#program to print the disctionary of lists   to   list of disctionaries;
def listDict(disc,length_check):
    temp_disc={}
    list_of_disc=[]
    for i in range(length_check):
    
        for key,values in disc.items():

            for j in values:
                temp_disc[key]=values[i]
                break
            # print(temp_disc)
        list_of_disc.append(temp_disc)
        temp_disc={}

    print("List of Dictionary :\n",list_of_disc)

disc={}
length_check=None
while key:=input("Enter Key of Disctionary(Press Enter to Exit):"):
    klist=[int(num) for num in (input("Enter comma seperated numbers:").split(","))]
    if length_check is None:
        length_check = len(klist)
    elif len(klist) != length_check:
        print(f"Error: Must enter  {length_check} Numbers. Please try again.")
        continue
    disc[key]=klist


# disc={'k1':[1,2,3],'k2':[4,5,6]}
print("Dictionary of list:\n",disc)

listDict(disc,length_check)

