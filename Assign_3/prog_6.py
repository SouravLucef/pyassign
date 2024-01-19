#program to print the disctionary of lists   to   list of disctionaries;

disc={'k1':[1,2,3],'k2':[4,5,6],'k3':[7,8,9]}
temp_disc={}
list_of_disc=[]
for i in range(len(disc.values())):
    
    for key,values in disc.items():

        for j in values:
            temp_disc[key]=values[i]
            break
        print(temp_disc)
    list_of_disc.append(temp_disc)
    temp_disc={}

print(list_of_disc)