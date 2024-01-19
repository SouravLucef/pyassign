disc= {'1':['a','b','c'], '2':['d','e','f'],'3':['g','h','i']}

# print(len(disc['1']))
# for i in disc['1']:
    
#     for j in disc['2']:
#         print(i+j)
l=list(disc.values())
print(l)
for i in range(len(l)-1):
    for j in l[i]:
        for k in l[i+1]:
            print(j+k)
'''for i in range(len(disc.values())-1):
    for key,value in disc.items():
        print(value[i],':',value[i+1])
        '''



