dis={
    'Name':["Sourav","Abhirup","Nirveek"],
    'Age':[23,22,21],
    'Salery':[10000,12000,15000]
}

for i,j in dis.items():
    print(i,end="\t")
    # for j in dis[i]:
    #     print (j,end=" ")
    
print("")
for i in dis:
    for j in dis[i]:
        print(j)
    print(end="\t")

        
