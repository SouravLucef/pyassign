disc= {'1':['a','b','c'], '2':['d','e','f'],'3':['g','h','i']}

l=list(disc.values())
print(l)
for i in range(len(l)-1):
    for j in l[i]:
        for k in l[i+1]:
            print(j+k)

